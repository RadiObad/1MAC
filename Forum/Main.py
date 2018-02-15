import Helper

mbrsHlpr = Helper.MembersManager()
mbrsHlpr.CreateMember("Mohammed", 31)
mbrsHlpr.CreateMember("Ahmed",25)
mbrsHlpr.CreateMember("Ismail",19)
mbrsHlpr.GetAllMembers()


postsHlpr = Helper.PostsManager()
postsHlpr.CreatePost("post1","this is my first post")
postsHlpr.CreatePost("post2","this my second post")
postsHlpr.CreatePost("post3","this is my third post")
postsHlpr.GetAllPosts()