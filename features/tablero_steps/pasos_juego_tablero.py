# -- FILE: features/steps/pasos_juego_cartas.py
from behave import given, when, then

@given('dos jugadores se han unido al juego')
def step_impl(context):
    print('      IMPLEMENTACION DE TABLERO - Dos jugadores sentados en la mesa')

@when('el primer jugador finaliza su turno')
def step_impl(context):
    print('      IMPLEMENTACION DE TABLERO - El jugador ha movido una pieza')

@then('el segundo jugador inicia su turno')
def step_impl(context):
    print('      IMPLEMENTACION DE TABLERO - El jugador toma una pieza')

