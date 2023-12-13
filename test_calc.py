import pytest

from calc import celsius_to_fahrenheit, fuel_consumption, megabit_to_megabyte, sigma, weight

#
# Degvielas patēriņš
#
def test_fuel_consumption_small():
    assert fuel_consumption(5, 50) == 10

def test_fuel_consumption_medium():
    assert fuel_consumption(8.5, 100) == 8.5

def test_fuel_consumption_big():
    assert fuel_consumption(49, 1000) == 4.9

#
# Mb to MB
#
def test_megabit_to_megabyte_zero():
    assert megabit_to_megabyte(0) == 0

def test_megabit_to_megabyte_small():
    assert megabit_to_megabyte(32) == 256

def test_megabit_to_megabyte_medium():
    assert megabit_to_megabyte(1024) == 8192

#
# Celsius to Fahrenheit
#
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(25) == 77

def test_celsius_to_fahrenheit_zero():
    assert celsius_to_fahrenheit(0) == 32

def test_celsius_to_fahrenheit_minus():
    assert celsius_to_fahrenheit(-25) == -13

#
# Sigma
#
def test_sigma_empty():
    assert sigma(0) == 0

# 3 + 2 + 1
def test_sigma_small():
    assert sigma(3) == 6

# 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
def test_sigma_medium():
    assert sigma(10) == 55

#
# Svars
#
def test_weight_grams():
    assert weight(100) == "100g"

def test_weight_kg():
    assert weight(79000) == "79kg"

def test_weight_kvintal():
    assert weight(700000) == "7c"

def test_weight_tons():
    assert weight(9000000) == "9t"
