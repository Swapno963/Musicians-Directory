# Musicians Directory Project

## Overview

The "Musicians Directory" project manages information about musicians and their albums. This project uses Django's class-based views and includes models for musicians and albums.

## Models

### Musician Model
- **First Name**
- **Last Name**
- **Email**
- **Phone Number**
- **Instrument Type**

### Album Model
- **Album Name**
- **Release Date**
- **Rating (1-5)**
- **Relationship with Musician Model (One-to-Many)**

## Functionality

- **Create:** Logged-in users can create new musicians and albums using model forms.
- **Edit:** Users can edit both musician and album data by clicking on the respective buttons.
- **Delete:** Users can delete album data using the delete button.
- **View:** Non-logged-in users can view the data in a table format without edit and delete permissions.

## Class-Based Views

- **MusicianListView:** Display a list of musicians.
- **MusicianCreateView:** Create a new musician.
- **MusicianUpdateView:** Update musician data.
- **MusicianDeleteView:** Delete musician data.
- **AlbumListView:** Display a list of albums.
- **AlbumCreateView:** Create a new album.
- **AlbumUpdateView:** Update album data.
- **AlbumDeleteView:** Delete album data.

## Instructions

1. **Editing Data:**
   - Click on the "Edit" button to edit album data.
   - Click on the name of the musician to edit musician data.

2. **Create New Data:**
   - Logged-in users can create new musicians and albums using the provided forms.

3. **Viewing Data:**
   - Non-logged-in users can view the table with musician and album information.

4. **Deleting Data:**
   - Users with appropriate permissions can delete album data using the "Delete" button.

5. **Saving Data:**
   - Data is saved to the backend automatically when users create or edit musicians and albums.

**Note:** Ensure you use Django's class-based views to implement the specified functionality.
