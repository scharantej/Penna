
# main.py

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database configuration
conn = sqlite3.connect('journal.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY,
                title TEXT,
                body TEXT,
                date TEXT,
                tags TEXT
            )''')
conn.commit()

# New entry page
@app.route('/new-entry', methods=['GET', 'POST'])
def new_entry():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        date = datetime.now().strftime('%Y-%m-%d')
        tags = request.form.getlist('tags')  # Multiple tags can be selected
        tags = ','.join(tags)  # Convert list to comma-separated string
        c.execute("INSERT INTO entries (title, body, date, tags) VALUES (?, ?, ?, ?)",
                  (title, body, date, tags))
        conn.commit()
        return redirect(url_for('entries'))
    return render_template('new-entry.html')

# List of entries page
@app.route('/entries')
def entries():
    c.execute("SELECT * FROM entries ORDER BY date DESC")
    entries = c.fetchall()
    return render_template('entries.html', entries=entries)

# Entry details page
@app.route('/entry-details/<int:entry_id>')
def entry_details(entry_id):
    c.execute("SELECT * FROM entries WHERE id = ?", (entry_id,))
    entry = c.fetchone()
    return render_template('entry-details.html', entry=entry)

# Edit entry page
@app.route('/edit-entry/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    c.execute("SELECT * FROM entries WHERE id = ?", (entry_id,))
    entry = c.fetchone()
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        date = datetime.now().strftime('%Y-%m-%d')
        tags = request.form.getlist('tags')
        tags = ','.join(tags)
        c.execute("UPDATE entries SET title = ?, body = ?, date = ?, tags = ? WHERE id = ?",
                  (title, body, date, tags, entry_id))
        conn.commit()
        return redirect(url_for('entries'))
    return render_template('edit-entry.html', entry=entry)

# Delete entry
@app.route('/delete-entry/<int:entry_id>')
def delete_entry(entry_id):
    c.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
    conn.commit()
    return redirect(url_for('entries'))

if __name__ == '__main__':
    app.run(debug=True)
