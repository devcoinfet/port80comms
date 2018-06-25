import urllib2
import base64

#compliment netmiko to achieve 22,23,80 manipulation
#take in ip user and pass create auth
def requester(ip,user,password):
    base64string = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
    req = urllib2.Request('http://'+ip+'/level/15/exec/-')
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; rv:59.0) Gecko/20100101 Firefox/59.0")
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    req.add_header("Accept-Language", "en-US,en;q=0.5")
    req.add_header("Accept-Encoding", "gzip, deflate")
    req.add_header("Referer", 'http://'+ip+'/level/15/exec/-')
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("DNT", "1")
    req.add_header("Authorization",'''Basic '''+base64string)
    req.add_header("Connection", "keep-alive")
    req.add_header("Upgrade-Insecure-Requests", "1")
    body = "command=show+ip+int+br&command_url=%2Flevel%2F15%2Fexec%2F-"
    try:
        #set timeout
       response = urllib2.urlopen(req, body,timeout=1)
       html = response.read()
       data = html.split()
       return data
    except:
        pass


def main():
    ip = "127.0.0.1"
    user = "cisco"
    password = "cisco"
    try:
       result = requester(ip,user,password)
       print(result)
    except:
       pass
main()
