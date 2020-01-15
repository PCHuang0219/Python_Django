# web
首次建立資料庫第一步: 
sudo apt-get update
sudo apt-get install mysql-server
可參考https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04

第2步:在資料庫中建立database　forum
進入資料庫指令:mysql -p密碼　-u root　
創建資料庫指令:CREATE DATABASE forum CHARACTER SET utf8;

第3步:將python資料移轉到mysql
python3 manage.py makemigrations
python3 manage.py migrate

若資料庫有問題，要重建(總共６步)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
進入資料庫 drop database forum
創建資料庫指令:CREATE DATABASE forum CHARACTER SET utf8;
python manage.py makemigrations
python manage.py migrate
