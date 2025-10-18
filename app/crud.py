from sqlmodel import select, Session
from .models import Link
from datetime import datetime

def create_link(session: Session, code: str, target_url: str, title: str | None = None) -> Link:
    link = Link(code=code, target_url=target_url, title=title)
    session.add(link)
    session.commit()
    session.refresh(link)
    return link


def get_link_by_code(session: Session, code: str) -> Link | None:
    statement = select(Link).where(Link.code == code)
    result = session.exec(statement).first()
    return result

def increment_click(session: Session, link: Link) -> None:
    link.click_count = (link.click_count or 0) + 1
    session.add(link)
    session.commit()


def get_all_link(session: Session) -> list[Link]:
    statement = select(Link)
    results = session.exec(statement).all()
    return results
