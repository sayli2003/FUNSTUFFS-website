import os

def read(dir,conn):
    cursor=conn.cursor()
    count =0 
    for file in os.listdir(dir):
        d = os.path.join(dir, file)
        if os.path.isdir(d):
           read(dir)
        else:
            if(file.endswith(".png") or file.endswith(".jpeg")):
                new=d[d.index("/static"):].replace("//","/")
                count +=1

                new_d ="INSERT INTO artwork VALUES ('new name','dfkasbfiluf bfhvb fdb hbviu bisud sbdiud scvusd  asycvid  cdisd  cvsdy sycvsuyd sdyvsds ysdfbdsc siysd asd duihdodc sdcbiy','"+new+"','"+"link"+str(count)+"')"
                cursor.execute('SELECT * FROM artwork WHERE link LIKE "'+new+'"')
                results = cursor.fetchall()
                print(len(results))
                if len(results)==0:
                    print(new_d)
                    cursor.execute(new_d)
                    # cursor.execute("DROP TABLE "+"link"+str(count))
                    # cursor.execute("CREATE TABLE "+"link"+str(count)+"(name,content)")
                    cursor.execute("INSERT INTO "+"link"+str(count)+" VALUES ('commenter 1','dfkasbfiluf bfhvb fdb hbviu bisud sbdiud scvusd  asycvid  cdisd  cvsdy sycvsuyd sdyvsds ysdfbdsc siysd asd duihdodc sdcbiy')")
                    cursor.execute("INSERT INTO "+"link"+str(count)+" VALUES ('commenter 2','dfkasbfiluf bfhvb fdb hbviu bisud sbdiud scvusd  asycvid  cdisd  cvsdy sycvsuyd sdyvsds ysdfbdsc siysd asd duihdodc sdcbiy')")
                    conn.commit()

def display(cursor):
    cursor.execute('SELECT * FROM artwork')
    results=cursor.fetchall()
    for result in results:
        print(result)
def getcomments(cursor,name):
    cursor.execute("SELECT * FROM "+name)
    results = cursor.fetchall()
    li=[]
    for result in results:
        dictionary={}
        dictionary['name']=result[0]
        dictionary['content']=result[1]
        li.append(dictionary)
    return li


def tolist(cursor,n):
    cursor.execute('SELECT * FROM artwork')
    results = cursor.fetchall()
    li=[]
    dictionary={}
    new_li=[]
    count=0
    for result in results:
        # new_li=[]
        count+=1
        dictionary={}
        dictionary['name']=result[0]
        dictionary['desp']=result[1]
        dictionary['img']=result[2]
        new_li.append(dictionary)
        if count==n and n!=0:
            li.append(new_li)
            new_li=[]
            count=0
        elif n==0:
            li=new_li
    return li

def find(x,cursor):
    cursor.execute('SELECT * FROM artwork WHERE title LIKE "' + x + '"')
    results=cursor.fetchall()
    if len(results) > 0:
        dictionary = {}
        dictionary['name'] = results[0][0]
        dictionary['desp'] = results[0][1]
        dictionary['img'] = results[0][2]
        dictionary['comments'] = results[0][3]
        return dictionary
    else:
        return False

#
# dir = "C://Users//Sayli//PycharmProjects//webdev//Funstuff//static//images"
# conn = sqlite3.connect('data.db')
# cursor = conn.cursor()
# # display(cursor)
# # li=tolist(cursor)
# # cursor.execute("CREATE TABLE artwork(title,description,link,comments)")
# # conn.commit()
# read(dir,cursor)
