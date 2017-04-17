#!/bin/python3

# Python library to manage RESTful LXD interface
# https://github.com/lxc/lxd/blob/master/doc/rest-api.md
import pylxd as lxd
import os


class Containers:

    def __init__(self):
        self.client = lxd.Client()


    def setup_container(self, name):
        # copy container
        config = {'name': name, 
                  'source': {'type': 'copy', 
                             'container_only': 'true',
                             'source': 'base-con'}}
        con = self.client.containers.create(config, wait=True)

        # add shared directory for unix socket fd
        con.devices['shareddir'] = {'type': 'disk',
                                    'source': os.getcwd() + '/src/' + name,
                                    'path': '/home'}
        # update container with changes
        con.save(wait=True)

        # copy archive file into container
        fd = open('rsc/' + name + '.tar.gz', 'rb')
        data = fd.read()
        con.files.put('/home/' + name + '.tar.gz', data)
        fd.close()

        # unpack archive with exec
        con.start(wait=True)
        command = ['tar', 'xf', '/home/' + name + '.tar.gz', 
                          '-C', '/home/']
        con.execute(command)

        # start autostart script
        command = ['bash', '-c', 'nohup bash /home/' + name + '/autostart.sh > /dev/null 2>&1 & exit']
        con.execute(command)
        con.stop(wait=True)


    def setup_players(self):
        # create LXD client interface
        try:
            # make sure base container exists and is stopped
            base_con = self.client.containers.get('base-con')
            base_con.stop(wait=True)
            
            

        except lxd.exceptions.LXDAPIException as err:
            print("Error: " + str(err))
