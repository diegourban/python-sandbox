def generate_invite_name(name):
    last_position = len(name)
    first_position = last_position - 4
    first_part = name[0:4]
    last_part = name[first_position:last_position]
    return first_part + ' ' + last_part

def send_invite(name):
    print 'Sending invite to %s' % name

def process_invite(name):
    formatted_name = generate_invite_name(name)
    send_invite(formatted_name)
