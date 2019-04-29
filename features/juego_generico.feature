Feature: Mostrar varias implementaciones con Behave
    
    Scenario: Turno de juego generico
    Given dos jugadores se han unido al juego
    When el primer jugador finaliza su turno
    Then el segundo jugador inicia su turno

