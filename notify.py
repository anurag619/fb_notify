import fbconsole

fbconsole.AUTH_SCOPE = ['manage_notifications', 'read_mailbox' ]
fbconsole.authenticate()

def notification():
    print 'fetching your unread notifications.... \n '
    notify = fbconsole.fql("SELECT is_unread,title_text FROM notification WHERE recipient_id=me()")
    for i in notify:
        list(i)
        a = i.values()
        if a[1]==1:
            print a[0]+'\n'

def unread():
    print 'showing number of unread messages in your inbox.... \n'
    unread = fbconsole.fql("SELECT unread_count FROM mailbox_folder WHERE folder_id =0 AND viewer_id =me()")
    print ' %s unread message(s) in your inbox' %(unread[0].values())

def main():
    print 'enter you choice:'
    a=raw_input('n--> for notification \n' 'r--> for unread messages \n')
    if a =='n':
        notification()
    elif a=='r':
        unread()
    else: 
        print 'wrong input'
        main()

if __name__=='__main__':
    main()


   



