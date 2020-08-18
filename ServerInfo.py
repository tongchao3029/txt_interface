ip = 'http://39.100.104.214'
port = '8080'

#path
register_path="/register/"
login_path="/login/"
create_path="/create/"
update_path="/update/"
getBlogsOfUser_path="/getBlogsOfUser/"
getBlogContent_path="/getBlogContent/"
getBlogsContent_path="/getBlogsContent/"
delete_path="/delete/"

register="%s:%s%s" %(ip,port,register_path)
login="%s:%s%s" %(ip,port,login_path)
create="%s:%s%s" %(ip,port,create_path)
getBlogsOfUser="%s:%s%s" %(ip,port,getBlogsOfUser_path)
update="%s:%s%s" %(ip,port,update_path)
getBlogContent="%s:%s%s" %(ip,port,getBlogContent_path)
getBlogsContent="%s:%s%s" %(ip,port,getBlogsContent_path)
delete="%s:%s%s" %(ip,port,delete_path)

if __name__=="__main__":
    print(eval("register"))
    print(eval("login"))
    print(eval("create"))
    print(eval("getBlogsOfUser"))
    print(eval("update"))
    print(eval("getBlogContent"))
    print(eval("getBlogsContent"))
    print(eval("delete"))
