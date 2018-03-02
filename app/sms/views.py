from django.shortcuts import render, redirect
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


def send_sms(request):
    if request.method == 'POST':
        # set api key, api secret
        api_key = "NCSGLMHSQ2FTVZUA"
        api_secret = "6SJTTSSM27RIGTG3ERVXKFLKVWVEUHFI"

        # 4 params(to, from, type, text) are mandatory. must be filled
        params = dict()
        params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
        params['to'] = request.POST['to_number'] # Recipients Number '01000000000,01000000001'
        params['from'] = '01044321237' # Sender number
        params['text'] = request.POST['msg'] # Message

        cool = Message(api_key, api_secret)
        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

        return redirect('send-sms')

    return render(request, 'sms/send.html')
