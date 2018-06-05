import requests
from ipaddress import ip_address, ip_network

def secIP():
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            return True
    else:
        return False
def secSIG(header_signature):
    if header_signature is None:
        return 'forbidden'

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return 'servererror'

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return 'forbidden'
