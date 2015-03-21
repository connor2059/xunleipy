#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from xunleipy.remote import XunLeiRemote


def remote_download(username, password, download_links, path='C:/TD/', peer=0):
    remote_client = XunLeiRemote(username, password)
    peer_list = remote_client.get_remote_peer_list()
    if len(peer_list) == 0:
        print 'No valid remote devices'
        return
    pid = peer_list[peer]['pid']
    return remote_client.add_urls_to_remote(pid, path, download_links)


if __name__ == '__main__':
    import sys
    download_link = sys.argv[1]
    with open('config.json', 'r') as f:
        import json
        config = json.load(f)
        username = config.get('username', '')
        password = config.get('password', '')
        if not username or not password:
            print 'Invalid username or password!'

        else:
            path = config.get('path', 'C:/TDDOWNLOAD/')
            print remote_download(username, password, [download_link])