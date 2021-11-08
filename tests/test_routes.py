'''#! This file will hold the tests for the code in our app/routes.py file.'''

def test_get_all_books_with_no_records(client):
    # passes client and will look up all the fixtures and find the client fixture
    # Act
    response = client.get("/books")
    # client sends a request to /books route
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    # checks the status code 
    assert response_body == []
    # what we want our asser to look like 

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }