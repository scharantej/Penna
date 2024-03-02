## Design for a Daily Journaling Flask Application

### HTML Files

1. **new-entry.html:**
   - Contains form for creating new journal entries.
   - Includes fields for title, body, date, and tags.
2. **entries.html:**
   - Lists all existing journal entries.
   - Displays title, date, and a brief excerpt of each entry.
   - Provides links to individual entry details pages.
3. **entry-details.html:**
   - Displays the full details of a specific journal entry.
   - Includes title, body, date, tags, and option to edit/delete.

### Routes

1. **new_entry:**
   - Route for handling new journal entry submission.
2. **entries:**
   - Route for fetching and displaying the list of all journal entries.
3. **entry_details(entry_id):**
   - Route for fetching and displaying a specific journal entry.
4. **edit_entry(entry_id):**
   - Route for handling editing of a specific journal entry.
5. **delete_entry(entry_id):**
   - Route for handling deletion of a specific journal entry.