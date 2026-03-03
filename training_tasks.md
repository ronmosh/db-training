# DB Training - Stage 1 Tasks

Welcome to the DB training exercise! This repository has a basic layered architecture (Controller -> Service -> Repository) and is connected to a PostgreSQL database via SQLAlchemy and Alembic.

Your team leader has reviewed the current structure and wants you to implement the following changes.

## Part 1: Bug Fixes and Small Adjustments

1. **Remove a Column**
   * **Task:** The team leader wants us to drop the `bio` column from authors. 
   * **Action:** Safely remove this field across all application layers and run a migration to drop it from the database schema.

2. **Change Field to Enum**
   * **Task:** We need a way to categorize our books. Add a `category` field to the books table.
   * **Action:** The column must enforce a strict Postgres Enum type (e.g. `'FICTION'`, `'NON_FICTION'`, `'SCIENCE'`). Update the DB schema and request structures accordingly.

3. **Fix the N+1 Query**
   * **Task:** When fetching authors (`GET /authors`), the system executes a separate query to retrieve books for *every* individual author.
   * **Action:** Optimize the query in the repository so both authors and their books are retrieved efficiently in a single database round-trip.

4. **Foreign Key Error Handling**
   * **Task:** The `POST /books` API does not elegantly handle scenarios where an author doesn't exist. It currently results in a 500 server error when PostgreSQL rejects the foreign key.
   * **Action:** Update the book creation flow to validate the author's existence before saving, returning a clean 404 HTTP exception instead.

---

## Part 2: Feature Requests

1. **Filter by Column**
   * **Task:** A dashboard requires finding authors by name prefix (e.g., "J.R.").
   * **Action:** Create a search endpoint returning a list of entities matching the requested `name_prefix`. 

2. **Pagination Strategy**
   * **Task:** The `GET /books` endpoint currently returns the entire table.
   * **Action:** Implement a standard pagination approach for this endpoint (skip, limit). Make sure to restrict the maximum returned rows per request to avoid overwhelming the system.

3. **Soft Deletes**
   * **Task:** Provide a safe deletion mechanism for authors.
   * **Action:** Update the authors table to support soft deletes. Write an endpoint to perform the soft deletion, and ensure all existing author retrieval endpoints automatically ignore soft-deleted records.

4. **Aggregate Data Endpoint**
   * **Task:** We need a report showing the total number of books per author.
   * **Action:** Expose an endpoint `GET /authors/stats` that efficiently computes this count. The computation should be offloaded completely to the database engine rather than counted in-memory.

---

## Part 3: Advanced Challenges

1. **Loop Insert Optimization**
   * **Task:** The marketing department has requested a bulk upload feature `POST /books/bulk` allowing them to upload 500 books at once.
   * **Action:** Your initial goal: write a naive implementation that loops over the payload and creates/commits each record individually. Then, document why this is bad, and implement a highly optimized bulk insert operation bypassing the ORM's heavy object tracking constraints.

2. **Many-to-Many Relationships**
   * **Task:** A single book can now have multiple tags, and tags can belong to multiple books.
   * **Action:** Design and implement a Many-to-Many relationship (creating the necessary join table via Alembic). Expose endpoints to assign tags to a book and to fetch tags for a book.

3. **Database Triggers**
   * **Task:** All tables should track when their records were last modified.
   * **Action:** Add an `updated_at` timestamp column to the authors table. Use Alembic to cleanly register a PostgreSQL trigger that automatically sets this timestamp on every row update. The logic must reside entirely in the database engine, not in the application.
