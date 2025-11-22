from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from typing import List

from db_class.models import User, AdminRole


async def list_users(db: AsyncSession) -> str:
    result = await db.execute(select(User))
    users = result.scalars().all()

    if not users:
        return "Пользователей пока нет."

    lines = []
    for u in users:
        parts = [u.first_name or "", u.last_name or "", u.patronymic or ""]
        full_name = " ".join(p for p in parts if p).strip()
        lines.append(f"{u.id}: {full_name or '—'} (tg_id={u.telegram_id})")

    return "Список пользователей:\n" + "\n".join(lines)



async def check_profile(db: AsyncSession) -> str:
    # грузим всех пользователей вместе с их ролью, без N+1
    result = await db.execute(
        select(User).options(
            selectinload(User.admin_role),
            selectinload(User.academic_role)
            )
    )
    users: List[User] = result.scalars().all()

    if not users:
        return "Пользователей пока нет."

    lines: list[str] = []
    for u in users:
        parts = [u.first_name or "", u.last_name or "", u.patronymic or ""]
        full_name = " ".join(p for p in parts if p).strip() or "—"

        admin_role_name = (
            u.admin_role.name  # подставь реальное поле: .name / .title / .code
            if u.admin_role is not None
            else "нет роли"
        )

        academic_role_name = (
            u.academic_role.name  # подставь реальное поле: .name / .title / .code
            if u.academic_role is not None
            else "нет роли"
        )

        lines.append(f"{u.id}: {full_name} — {academic_role_name} — {admin_role_name}")

    return "Пользователи:\n" + "\n".join(lines)