import models

class MembersManager:
    members = []
    def CreateMember(self,name,age):
        member = models.Member(name,age)
        self.members.append(member)    
    def AddMember(self,member):
        self.members.append(member)    
    def GetAllMembers(self):
        for member in self.members:
            print "Name: {0} || Age: {1}".format(member.Name,member.Age)           

class PostsManager:
	posts = []
	def CreatePost(self,title,content):
		post = models.Post(title,content)
		self.posts.append(post)	
	def AddPost(self,post):
		self.posts.append(post)
	def GetAllPosts(self) :       
          for post in self.posts:
            print "Post:{0} || content:{1}".format(post.Title,post.Content)	 	
