"""Testes adicionais: desempate do ranking de hotéis."""

from helpers import run_cli


def test_top_hotels_tie_breaks_by_hotel_id_ascending(tmp_path):
    """total_brl decrescente; empate por hotel_id ascendente (README > Ordenação)."""
    report = run_cli(
        tmp_path,
        [
            {"reservation_id": "R-1", "hotel_id": "H02", "hotel_name": "Hotel B", "amount": "500.00"},
            {"reservation_id": "R-2", "hotel_id": "H03", "hotel_name": "Hotel C", "amount": "1000.00"},
            {"reservation_id": "R-3", "hotel_id": "H01", "hotel_name": "Hotel A", "amount": "500.00"},
        ],
        top=3,
    )
    assert [hotel["hotel_id"] for hotel in report["top_hotels"]] == ["H03", "H01", "H02"]