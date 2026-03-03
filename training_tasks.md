# DB Training - Stage 1 Tasks

Welcome to the DB training exercise! This repository has a basic layered architecture (Controller -> Service -> Repository) and is connected to a PostgreSQL database via SQLAlchemy and Alembic.

Your team leader has reviewed the current structure and wants you to implement the following changes.

## Part 1: Bug Fixes and Small Adjustments

1. **Remove a Column**
   * **Task:** The team leader wants to remove the `bio` column from the `authors` table. 
   * **Action:** Update the SQLAlchemy model, the Pydantic entities, and generate an Alembic migration for this removal.

2. **Change Field to Enum**
   * **Task:** We need to categorize books. Add a `category` field to the `books` table, but it should be a strict PostgreSQL `ENUM` type (e.g., `'FICTION'`, `'NON_FICTION'`, `'SCIENCE'`). 
   * **Action:** Update the model to use `sqlalchemy.Enum`, add the field to Pydantic entities, and generate the Alembic migration.

3. **Fix the N+1 Books Problem**
   * **Task:** When fetching an author, we also want to display their books. However, right now it either doesn't return them or executes a new query for every author.
   * **Action:** Fix this by modifying the repository to use `joinedload` for the `books` relationship and update the response entity to include a list of books.

4. **Add Data Validation**
   * **Task:** The `POST /books` endpoint currently allows saving a book even if the `author_id` doesn't exist in the database, which causes a 500 integrity error.
   * **Action:** Fix this bug in `services/book.py` by checking if the author exists *before* attempting to create the book. If not found, raise a `404 Not Found` HTTP exception.

---

## Part 2: Feature Requests

1. **Filter by Column**
   * **Task:** Have a way to get all the Entity A that has X in this column. 
   * **Action:** Add a new endpoint `GET /authors/search` that takes a query parameter `name_prefix` and returns all authors whose name starts with that prefix.

2. **Pagination Strategy**
   * **Task:** The `GET /books` endpoint might return too many records in the future.
   * **Action:** Implement pagination for the `GET /books` endpoint. Add `skip` and `limit` query parameters, ensuring `limit` has a max constraint of 100. Update the repository to handle offset and limit.

3. **Soft Deletes**
   * **Task:** We don't want to completely delete authors from the database, but we want a way to "remove" them.
   * **Action:** Add an `is_deleted` boolean column to the `authors` table (default `False`). Create an endpoint `DELETE /authors/{id}` that sets this flag to `True`. Make sure all `GET` operations filter out deleted authors.

4. **Aggregate Data Endpoint**
   * **Task:** The dashboard needs to know how many books each author has.
   * **Action:** Create an endpoint `GET /authors/stats` that returns a list of authors along with a `book_count` field. Implement this optimally in the repository using SQL `GROUP BY` rather than counting in Python.
