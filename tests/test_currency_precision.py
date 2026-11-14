"""Testes adicionais: conversão de câmbio exata com Decimal (sem float)."""

from helpers import run_cli


def test_currency_conversion_is_exact_with_half_up(tmp_path):
    """18.25 USD * 5.42 = 98.915 exatos -> half-up "98.92".

    Em float o produto vira 98.91499999999999 e arredondaria para "98.91".
    """
    report = run_cli(
        tmp_path,
        [{"reservation_id": "R-1", "currency": "USD", "amount": "18.25"}],
    )
    assert report["summary"]["total_amount_brl"] == "98.92"
    assert report["by_month"][0]["total_brl"] == "98.92"
    assert report["top_hotels"][0]["total_brl"] == "98.92"