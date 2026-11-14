"""Testes adicionais: noites de quarto na virada de ano, com mais de um quarto."""

from helpers import run_cli


def test_nights_across_year_boundary_with_multiple_rooms(tmp_path):
    """30/12 -> 02/01 são 3 noites; com 2 quartos, 6 room nights (README: vale na virada de ano)."""
    report = run_cli(
        tmp_path,
        [
            {
                "reservation_id": "R-1",
                "checkin_date": "2024-12-30",
                "checkout_date": "2025-01-02",
                "rooms": "2",
            }
        ],
    )
    assert report["summary"]["total_room_nights"] == 6
    assert report["by_month"][0]["month"] == "2024-12"
    assert report["by_month"][0]["room_nights"] == 6