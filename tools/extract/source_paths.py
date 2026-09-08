"""数学大問の原本パスを設定から解決する。"""

from __future__ import annotations

from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
GITHUB = REPO.parent
DATABASE = GITHUB / "koukou-nyushi-database"


def _override_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else DATABASE / path


def source_paths(config: dict) -> tuple[Path, Path]:
    """問題・解説を含む数学PDFと解答用紙PDFを返す。"""

    problem_override = config.get("problem_source_pdf")
    answer_override = config.get("answer_source_pdf")
    if problem_override or answer_override:
        if not problem_override or not answer_override:
            raise ValueError(
                f"{config.get('slug', '(unknown)')}: "
                "problem_source_pdf と answer_source_pdf は両方指定してください"
            )
        problem = _override_path(problem_override)
        answer = _override_path(answer_override)
    else:
        repo_name = config.get("repo")
        if not repo_name:
            raise ValueError(
                f"{config.get('slug', '(unknown)')}: repo または原本PDFを指定してください"
            )
        base = GITHUB / repo_name / "public" / "files" / str(config["year"])
        problem = base / "解説付き問題" / "数学.pdf"
        answer = base / "解答用紙" / "数学.pdf"

    if not problem.is_file() or not answer.is_file():
        raise FileNotFoundError(f"原本がありません: {problem} / {answer}")
    return problem, answer


def section_source_path(config: dict, section: str, problem_source: Path) -> Path:
    """正解・解説の別PDF指定を解決する。未指定時は問題PDFを使う。"""

    keys = {
        "answers": "answers_source_pdf",
        "explanation": "explanation_source_pdf",
    }
    try:
        key = keys[section]
    except KeyError as error:
        raise ValueError(f"未対応のセクションです: {section}") from error
    value = config.get(key)
    source = _override_path(value) if value else problem_source
    if not source.is_file():
        raise FileNotFoundError(
            f"{config.get('slug', '(unknown)')}: {section} 原本がありません: {source}"
        )
    return source
