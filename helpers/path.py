def path_split(path):
        import os
        # Get the drive (e.g., 'C:')
        drive, remainder_path = os.path.splitdrive(path)

        # Normalize the path to handle special characters
        remainder_path = os.path.normpath(remainder_path)

        # Get the folders (list)
        folders = []
        while True:
            remainder_path, folder = os.path.split(remainder_path)
            if not folder:
                break
            folders.insert(0, folder)

        # Get the file name and extension
        file_name, file_extension = os.path.splitext(os.path.basename(path))

        # Print the results
        print("Drive:", drive)
        print("Folders:", folders)
        print("File name:", file_name)
        print("Extension:", file_extension)

        return drive, folders, file_name, file_extension
