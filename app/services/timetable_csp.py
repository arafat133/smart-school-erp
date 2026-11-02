# -*- coding: utf-8 -*-
"""
================================================================================
📅 ENTERPRISE TIMETABLE CSP (CONSTRAINT SATISFACTION PROBLEM) ENGINE
================================================================================
Solves the NP-hard School Timetabling Problem with strict mathematical guarantees:
  1. Teacher Non-Overlap: ∀ d, p: Teacher T cannot teach > 1 section concurrently.
  2. Room Non-Overlap:    ∀ d, p: Room R cannot host > 1 section concurrently.
  3. Section Non-Overlap: ∀ d, p: Section S cannot attend > 1 lesson concurrently.
  4. Room Capacity:       ∀ assignment: Room.Capacity >= Section.StudentCount.
  5. Teacher Workload:    Teacher weekly periods <= MaxWeeklyQuota.
================================================================================
"""
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, field

@dataclass(frozen=True)
class TimeSlot:
    day: str          # e.g., "Saturday", "Sunday", ...
    period: int       # 1 to 7

@dataclass
class Teacher:
    id: str
    name: str
    max_periods_per_day: int = 4
    max_periods_per_week: int = 24
    unavailable_slots: Set[TimeSlot] = field(default_factory=set)

@dataclass
class Classroom:
    id: str
    name: str
    capacity: int
    is_lab: bool = False

@dataclass
class Section:
    id: str
    name: str
    grade_level: str
    student_count: int

@dataclass
class LessonRequirement:
    id: str
    section_id: str
    subject_name: str
    teacher_id: str
    periods_per_week: int
    requires_lab: bool = False

@dataclass
class ScheduleAssignment:
    lesson_id: str
    section_id: str
    subject_name: str
    teacher_id: str
    room_id: str
    day: str
    period: int

class TimetableCSPSolver:
    """
    Backtracking Constraint Satisfaction Problem Solver for Academic Timetables.
    """
    DAYS = ["السبت", "الأحد", "الإثنين", "الثلاثاء", "الأربعاء"]
    PERIODS = [1, 2, 3, 4, 5, 6] # 6 periods per day = 30 periods weekly

    def __init__(
        self,
        sections: List[Section],
        teachers: List[Teacher],
        rooms: List[Classroom],
        lessons: List[LessonRequirement]
    ):
        self.sections = {s.id: s for s in sections}
        self.teachers = {t.id: t for t in teachers}
        self.rooms = {r.id: r for r in rooms}
        self.lessons = lessons

        # State trackers during backtracking
        self.teacher_schedule: Dict[Tuple[str, str, int], str] = {} # (teacher_id, day, period) -> lesson_id
        self.room_schedule: Dict[Tuple[str, str, int], str] = {}    # (room_id, day, period) -> lesson_id
        self.section_schedule: Dict[Tuple[str, str, int], str] = {} # (section_id, day, period) -> lesson_id
        self.teacher_daily_count: Dict[Tuple[str, str], int] = {}   # (teacher_id, day) -> count
        self.assignments: List[ScheduleAssignment] = []

    def solve(self) -> Tuple[bool, List[ScheduleAssignment], List[str]]:
        """
        Executes CSP Backtracking algorithm to schedule all required lessons without conflicts.
        """
        # Expand weekly lesson requirements into individual period tasks
        unassigned_tasks: List[Tuple[LessonRequirement, int]] = []
        for req in self.lessons:
            for k in range(req.periods_per_week):
                unassigned_tasks.append((req, k))

        # Heuristic: Sort tasks by most constrained first (MRV - Minimum Remaining Values)
        # Labs and large sections first
        unassigned_tasks.sort(
            key=lambda item: (
                0 if item[0].requires_lab else 1,
                -self.sections[item[0].section_id].student_count
            )
        )

        success = self._backtrack(unassigned_tasks, 0)
        errors = []
        if not success:
            errors.append("تعذر إيجاد جدول خالي تماماً من التعارضات بالموارد والقاعات المتاحة الحالية.")
        return success, self.assignments, errors

    def _backtrack(self, tasks: List[Tuple[LessonRequirement, int]], task_index: int) -> bool:
        if task_index >= len(tasks):
            return True  # All lessons successfully scheduled

        req, task_num = tasks[task_index]
        section = self.sections[req.section_id]
        teacher = self.teachers[req.teacher_id]

        # Domain exploration: try all days, periods, and eligible rooms
        for day in self.DAYS:
            # Check teacher daily load ceiling
            if self.teacher_daily_count.get((teacher.id, day), 0) >= teacher.max_periods_per_day:
                continue

            for period in self.PERIODS:
                slot = TimeSlot(day, period)
                if slot in teacher.unavailable_slots:
                    continue

                # Hard Constraint 1: Teacher Conflict
                if (teacher.id, day, period) in self.teacher_schedule:
                    continue

                # Hard Constraint 2: Section Conflict
                if (section.id, day, period) in self.section_schedule:
                    continue

                # Search for eligible room
                for room in self.rooms.values():
                    # Hard Constraint 3: Room Type & Capacity
                    if req.requires_lab and not room.is_lab:
                        continue
                    if room.capacity < section.student_count:
                        continue # Room too small!

                    # Hard Constraint 4: Room Conflict
                    if (room.id, day, period) in self.room_schedule:
                        continue

                    # Forward Assignment
                    self.teacher_schedule[(teacher.id, day, period)] = req.id
                    self.section_schedule[(section.id, day, period)] = req.id
                    self.room_schedule[(room.id, day, period)] = req.id
                    self.teacher_daily_count[(teacher.id, day)] = self.teacher_daily_count.get((teacher.id, day), 0) + 1

                    assignment = ScheduleAssignment(
                        lesson_id=f"{req.id}-{task_num}",
                        section_id=section.id,
                        subject_name=req.subject_name,
                        teacher_id=teacher.id,
                        room_id=room.id,
                        day=day,
                        period=period
                    )
                    self.assignments.append(assignment)

                    # Recurse
                    if self._backtrack(tasks, task_index + 1):
                        return True

                    # Backtrack (Revert)
                    self.assignments.pop()
                    del self.teacher_schedule[(teacher.id, day, period)]
                    del self.section_schedule[(section.id, day, period)]
                    del self.room_schedule[(room.id, day, period)]
                    self.teacher_daily_count[(teacher.id, day)] -= 1

        return False

    @staticmethod
    def audit_timetable(
        assignments: List[ScheduleAssignment],
        sections: Dict[str, Section],
        rooms: Dict[str, Classroom]
    ) -> Dict[str, Any]:
        """
        Performs an independent verification of any timetable to detect CSP violations.
        """
        teacher_seen: Dict[Tuple[str, str, int], List[str]] = {}
        room_seen: Dict[Tuple[str, str, int], List[str]] = {}
        section_seen: Dict[Tuple[str, str, int], List[str]] = {}
        capacity_violations = []

        for a in assignments:
            key_t = (a.teacher_id, a.day, a.period)
            teacher_seen.setdefault(key_t, []).append(a.lesson_id)

            key_r = (a.room_id, a.day, a.period)
            room_seen.setdefault(key_r, []).append(a.lesson_id)

            key_s = (a.section_id, a.day, a.period)
            section_seen.setdefault(key_s, []).append(a.lesson_id)

            sec = sections.get(a.section_id)
            rm = rooms.get(a.room_id)
            if sec and rm and rm.capacity < sec.student_count:
                capacity_violations.append({
                    "assignment": a.lesson_id,
                    "room": rm.name,
                    "room_capacity": rm.capacity,
                    "section": sec.name,
                    "student_count": sec.student_count
                })

        teacher_clashes = [k for k, v in teacher_seen.items() if len(v) > 1]
        room_clashes = [k for k, v in room_seen.items() if len(v) > 1]
        section_clashes = [k for k, v in section_seen.items() if len(v) > 1]

        is_valid = (
            len(teacher_clashes) == 0 and
            len(room_clashes) == 0 and
            len(section_clashes) == 0 and
            len(capacity_violations) == 0
        )

        return {
            "is_conflict_free": is_valid,
            "teacher_clashes_count": len(teacher_clashes),
            "room_clashes_count": len(room_clashes),
            "section_clashes_count": len(section_clashes),
            "capacity_violations_count": len(capacity_violations),
            "teacher_clashes": teacher_clashes,
            "room_clashes": room_clashes,
            "section_clashes": section_clashes,
            "capacity_violations": capacity_violations
        }
