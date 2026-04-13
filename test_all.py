import math

import pytest

import lap_timer
import lap_timer_client

# ======================
# lap_timer.py (44 puntos)
# ======================


@pytest.mark.points(3)
def test_init_crea_estructura_basica():
    timer = lap_timer.init(10)
    assert timer == {"max": 10, "times": [], "total": 0.0}


@pytest.mark.points(3)
def test_init_guarda_max_laps():
    timer = lap_timer.init(3)
    assert timer["max"] == 3


@pytest.mark.points(2)
def test_add_lap_agrega_vuelta():
    timer = lap_timer.init(5)
    lap_timer.add_lap(timer, 1.23)
    assert timer["times"] == [1.23]


@pytest.mark.points(2)
def test_add_lap_actualiza_total():
    timer = lap_timer.init(5)
    lap_timer.add_lap(timer, 1.0)
    lap_timer.add_lap(timer, 2.5)
    assert math.isclose(timer["total"], 3.5)


@pytest.mark.points(2)
def test_add_lap_retorna_mismo_diccionario():
    timer = lap_timer.init(5)
    returned = lap_timer.add_lap(timer, 0.8)
    assert returned is timer


@pytest.mark.points(1.5)
def test_count_bolt_100m():
    timer = lap_timer.init(10)
    for t in [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.90]:
        lap_timer.add_lap(timer, t)
    assert lap_timer.count(timer) == 10


@pytest.mark.points(1.5)
def test_count_con_una_vuelta():
    timer = lap_timer.init(3)
    lap_timer.add_lap(timer, 4.2)
    assert lap_timer.count(timer) == 1


@pytest.mark.points(2)
def test_cumulative_time_bolt_100m():
    timer = lap_timer.init(10)
    for t in [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.90]:
        lap_timer.add_lap(timer, t)
    assert math.isclose(lap_timer.cumulative_time(timer), 9.69)


@pytest.mark.points(2)
def test_cumulative_time_suma_simple():
    timer = lap_timer.init(4)
    for t in [2.0, 2.0, 2.0]:
        lap_timer.add_lap(timer, t)
    assert math.isclose(lap_timer.cumulative_time(timer), 6.0)


@pytest.mark.points(2.5)
def test_format_laps_formato_exacto_bolt():
    timer = lap_timer.init(10)
    for t in [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.90]:
        lap_timer.add_lap(timer, t)
    assert (
        lap_timer.format_laps(timer)
        == "[1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.9]"
    )


@pytest.mark.points(2.5)
def test_format_laps_varios_decimales():
    timer = lap_timer.init(3)
    for t in [3.14159, 2.0, 2.5]:
        lap_timer.add_lap(timer, t)
    assert lap_timer.format_laps(timer) == "[3.14159, 2.0, 2.5]"


@pytest.mark.points(2)
def test_fastest_lap_bolt_100m():
    timer = lap_timer.init(10)
    for t in [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.90]:
        lap_timer.add_lap(timer, t)
    assert math.isclose(lap_timer.fastest_lap(timer), 0.82)


@pytest.mark.points(2)
def test_fastest_lap_caso_simple():
    timer = lap_timer.init(4)
    for t in [5.0, 3.0, 7.0]:
        lap_timer.add_lap(timer, t)
    assert math.isclose(lap_timer.fastest_lap(timer), 3.0)


@pytest.mark.points(2)
def test_fastest_multi_lap_bolt_k5():
    timer = lap_timer.init(10)
    for t in [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.90]:
        lap_timer.add_lap(timer, t)
    assert math.isclose(lap_timer.fastest_multi_lap(timer, 5), 4.14)


@pytest.mark.points(2)
def test_fastest_multi_lap_k1_equivale_a_fastest_lap():
    timer = lap_timer.init(5)
    for t in [4.0, 3.0, 2.0, 5.0]:
        lap_timer.add_lap(timer, t)
    assert math.isclose(lap_timer.fastest_multi_lap(timer, 1), 2.0)


@pytest.mark.points(2)
def test_fastest_multi_lap_k_total_equivale_total():
    timer = lap_timer.init(4)
    for t in [1.0, 2.0, 3.0, 4.0]:
        lap_timer.add_lap(timer, t)
    assert math.isclose(lap_timer.fastest_multi_lap(timer, 4), 10.0)


@pytest.mark.points(2)
def test_fastest_multi_lap_mejor_ventana_al_medio():
    timer = lap_timer.init(6)
    for t in [9.0, 1.0, 1.5, 1.0, 8.0, 8.0]:
        lap_timer.add_lap(timer, t)
    assert math.isclose(lap_timer.fastest_multi_lap(timer, 3), 3.5)


@pytest.mark.points(2)
def test_longest_decreasing_streak_bolt_100m():
    timer = lap_timer.init(10)
    for t in [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.90]:
        lap_timer.add_lap(timer, t)
    assert lap_timer.longest_decreasing_streak(timer) == 6


@pytest.mark.points(2)
def test_longest_decreasing_streak_agnel_400m():
    timer = lap_timer.init(8)
    for t in [26.12, 25.53, 25.21, 25.18, 25.42, 25.31, 25.26, 25.37]:
        lap_timer.add_lap(timer, t)
    assert lap_timer.longest_decreasing_streak(timer) == 4


@pytest.mark.points(2)
def test_longest_decreasing_streak_ledecky_1500m():
    timer = lap_timer.init(30)
    for t in [
        31.63, 31.21, 30.98, 30.85, 30.72, 30.58, 30.61, 30.55, 30.48, 30.52,
        30.49, 30.45, 30.51, 30.48, 30.42, 30.55, 30.52, 30.49, 30.46, 30.43,
        30.48, 30.52, 30.49, 30.45, 30.51, 30.55, 30.52, 30.58, 30.62, 29.98,
    ]:
        lap_timer.add_lap(timer, t)
    assert lap_timer.longest_decreasing_streak(timer) == 6


@pytest.mark.points(2)
def test_longest_decreasing_streak_todas_iguales():
    timer = lap_timer.init(4)
    for t in [2.0, 2.0, 2.0, 2.0]:
        lap_timer.add_lap(timer, t)
    assert lap_timer.longest_decreasing_streak(timer) == 1


# ============================
# lap_timer_client.py (6 puntos)
# ============================


@pytest.mark.points(2)
def test_client_lee_n_e_inicializa_timer(monkeypatch, tmp_path):
    path = tmp_path / "entrada.txt"
    path.write_text("3\n1.1\n1.2\n1.3\n", encoding="utf-8")

    calls = {"init": None, "add": []}

    def fake_init(n):
        calls["init"] = n
        return {"max": n, "times": [], "total": 0.0}

    def fake_add(timer, t):
        calls["add"].append(t)
        return timer

    monkeypatch.setattr(lap_timer_client.lap_timer, "init", fake_init)
    monkeypatch.setattr(lap_timer_client.lap_timer, "add_lap", fake_add)
    monkeypatch.setattr(
        lap_timer_client.lap_timer,
        "longest_decreasing_streak",
        lambda timer: 0,
    )
    monkeypatch.setattr("builtins.input", lambda _prompt: str(path))

    lap_timer_client.main()

    assert calls["init"] == 3


@pytest.mark.points(2)
def test_client_agrega_tiempos_en_orden(monkeypatch, tmp_path):
    path = tmp_path / "entrada.txt"
    path.write_text("4\n2.5\n2.0\n1.8\n2.1\n", encoding="utf-8")

    calls = []

    monkeypatch.setattr(lap_timer_client.lap_timer, "init", lambda n: {"n": n})
    monkeypatch.setattr(
        lap_timer_client.lap_timer,
        "add_lap",
        lambda timer, t: (calls.append(t) or timer),
    )
    monkeypatch.setattr(
        lap_timer_client.lap_timer,
        "longest_decreasing_streak",
        lambda timer: 0,
    )
    monkeypatch.setattr("builtins.input", lambda _prompt: str(path))

    lap_timer_client.main()

    assert calls == [2.5, 2.0, 1.8, 2.1]


@pytest.mark.points(2)
def test_client_imprime_resultado_de_racha(monkeypatch, tmp_path, capsys):
    path = tmp_path / "entrada.txt"
    path.write_text("1\n9.99\n", encoding="utf-8")

    monkeypatch.setattr(lap_timer_client.lap_timer, "init", lambda n: {"n": n})
    monkeypatch.setattr(lap_timer_client.lap_timer, "add_lap", lambda timer, t: timer)
    monkeypatch.setattr(
        lap_timer_client.lap_timer,
        "longest_decreasing_streak",
        lambda timer: 7,
    )
    monkeypatch.setattr("builtins.input", lambda _prompt: str(path))

    lap_timer_client.main()
    out = capsys.readouterr().out

    assert out.strip().endswith("7")
