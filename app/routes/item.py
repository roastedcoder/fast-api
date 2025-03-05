from fastapi import APIRouter, Depends, HTTPException
from typing import List
from enum import Enum

router = APIRouter()

class AvailableCuisine(str, Enum):
    indian = "indian"
    mexican = "mexican"
    italian = "italian"

class AvailableCoupon(int, Enum):
    coupon_10 = 1
    coupon_20 = 2
    coupon_30 = 3

coupon_codes = {
    1: "10%",
    2: "20%",
    3: "30%",
}

food_items = {
    "indian": ["biryani", "tandoori chicken", "naan"],
    "mexican": ["tacos", "burritos", "tamales"],
    "italian": ["pizza", "pasta", "risotto"],
}

@router.get("/items/{cuisine}")
def get_item(cuisine: AvailableCuisine):
    return food_items.get(cuisine)

@router.get("/items/")
def get_items():
    return food_items

@router.get("/items/coupon/{code}")
def get_items(code: int):
    return coupon_codes.get(code)