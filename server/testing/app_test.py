# server/testing/app_test.py
import json
import pytest
from app import app, db, Plant

def test_plant_by_id_get_route(client):
    '''has a resource available at "/plants/<int:id>".'''
    response = client.get('/plants/1')
    assert response.status_code == 200

def test_plant_by_id_get_route_returns_one_plant(client):
    '''returns JSON representing one Plant object at "/plants/<int:id>".'''
    response = client.get('/plants/1')
    data = json.loads(response.data.decode())
    
    assert isinstance(data, dict)
    assert 'id' in data

def test_plant_by_id_patch_route_updates_is_in_stock(client):
    '''returns JSON representing updated Plant object with "is_in_stock" = False at "/plants/<int:id>".'''
    # First, fetch the existing plant
    response = client.get('/plants/1')
    data = json.loads(response.data.decode())
    
    # Check initial state
    assert data["is_in_stock"] is True
    
    # Update the plant
    response = client.patch('/plants/1', json={'is_in_stock': False})
    assert response.status_code == 200
    
    # Fetch the updated plant
    response = client.get('/plants/1')
    data = json.loads(response.data.decode())
    
    # Check updated state
    assert data["is_in_stock"] is False
