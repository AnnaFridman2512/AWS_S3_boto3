import os
import boto3
from botocore.exceptions import NoCredentialsError

s3 = boto3.client('s3', region_name='us-west-2')


def create_s3_bucket(bucket_name):
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    })
    print(f"S3 bucket {bucket_name} created successfully")


def upload_file_to_s3(file_path, bucket_name):
    # Expand the tilde character in the file path to the user's home directory
    file_path = os.path.expanduser(file_path)
    try:
        s3.upload_file(file_path, bucket_name, file_path.split("/")[-1])  # split gets the filename
        print(f"File {file_path} uploaded to S3 bucket {bucket_name} successfully!")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except NoCredentialsError:
        print("Credentials not available to upload file to S3.")


def upload_files_to_s3(directory_path, bucket_name):
    # Expand the tilde character in the directory path to the user's home directory
    directory_path = os.path.expanduser(directory_path)

    # Get a list of all files in the directory
    paths_to_files = []
    for file in os.listdir(directory_path):
        full_path = os.path.join(directory_path, file) #construct the path
        if os.path.isfile(full_path): #check if its a file (other directories can be in the directory)
            paths_to_files.append(full_path)

    # Upload each file to the S3 bucket
    for path_to_file in paths_to_files:
        try:
            s3.upload_file(path_to_file, bucket_name, os.path.basename(path_to_file)) #basename(path_to_file) - creates the key to the object-will be named same as filename
            print(f"File {path_to_file} uploaded to S3 bucket {bucket_name} successfully!")
        except NoCredentialsError:
            print("Credentials not available to upload file to S3.")


def download_file_from_s3(bucket_name, file_name, download_path):
    print(bucket_name, file_name, download_path)


def list_s3_objects(bucket_name):
    print(bucket_name)


def delete_s3_bucket(bucket_name):
    print(bucket_name)


while True:
    print("What would you like to do?")
    print("1. create_s3_bucket")
    print("2. upload_file_to_s3")
    print("3. upload_files_to_s3")
    print("4. download_file_from_s3")
    print("5. list_s3_objects")
    print("6. delete_s3_bucket")
    print("7. EXIT")

    choice = input("Please Enter your choice (1/2/3...): ")
    if 1 <= int(choice) <= 6:
        bucket_name = input("Please enter bucket name: ")

        if choice == "1":
            create_s3_bucket(bucket_name)
            break
        elif choice == "2":
            file_path = input("Please enter file path: ")
            upload_file_to_s3(file_path, bucket_name)
            break
        elif choice == "3":
            directory_path = input("Please enter directory path: ")
            upload_files_to_s3(directory_path, bucket_name)
            break
        elif choice == "4":
            file_name = input("Enter filename to download: ")
            download_path = input("Please enter path to file: ")
            download_file_from_s3(bucket_name, file_name, download_path)
            break
        elif choice == "5":
            list_s3_objects(bucket_name)
            break
        elif choice == "6":
            delete_s3_bucket(bucket_name)
            break
    elif choice == "7":
        print("Exiting program")
        break
    else:
        print("Enter valid selection (1/2/3...)")
