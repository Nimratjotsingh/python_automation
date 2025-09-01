from fabric.api import *

def webhost():
    print("Welcome to the script\n")
    print("Downloading httpd")
    sudo("yum install httpd wget unzip -y")
    sudo("mkdir -p /tmp/webtry")
    with cd("/tmp/webtry"):
        webinp = input("Enter your website URL: ")
        foldername = input("Enter the folder name: ")
        sudo(f"wget {webinp}")
        sudo(f"unzip {foldername}.zip")
        sudo("systemctl start httpd && systemctl enable httpd")
        sudo(f"mv {foldername}/* /var/www/html")
        sudo("systemctl restart httpd")

    print("Task executed successfully")
