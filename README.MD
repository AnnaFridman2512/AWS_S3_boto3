You have been asked to write a Python script to automate the backup process of a
company's website files. The website files are hosted on an S3 bucket named
"my-bucket", which contains a large number of files and directories.
Write a Python script that allows the user to choose one of the following actions to
perform on the S3 bucket "my-bucket" using Boto3 : ( some functions may be need OS
also )
1. Create a new S3 bucket named "my-new-bucket".
( you have to choose the bucket name, remember that the bucket name should
be unique )
2. Upload a single file named "my-file.txt" to the existing S3 bucket named
"my-bucket".
3. Upload multiple files to the existing S3 bucket named "my-bucket".
4. Download the file named "my-file.txt" from the existing S3 bucket named
"my-bucket".
5. List all the objects in the existing S3 bucket named "my-bucket".
6. Delete the existing S3 bucket named "my-bucket".
Write a separate function for each action:
1. create_s3_bucket(bucket_name)
● This function should create a new S3 bucket with the given name.
2. upload_file_to_s3(file_path, bucket_name)
● This function should upload a single file to the given S3 bucket.
3. upload_files_to_s3(directory_path, bucket_name)
● This function should upload all the files in the given directory to the given
S3 bucket.
4. download_file_from_s3(bucket_name, file_name, download_path)
● This function should download the given file from the given S3 bucket to
the specified path.
5. list_s3_objects(bucket_name)
● This function should list all the objects in the given S3 bucket.
6. delete_s3_bucket(bucket_name)
● This function should delete the given S3 bucket.
The script should prompt the user to enter a number corresponding to the action they
want to perform. After the user enters their choice, the script should call the
corresponding function to execute the action using Boto3.
*** the script should run on VM CLI.