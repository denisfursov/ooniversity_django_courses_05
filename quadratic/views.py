from django.shortcuts import render
import math


def get_val_data(a):
    error_a = ''
    error_not_int = 'коэффициент не целое число'
    error_null = 'коэффициент не определен'
    error_zero = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    if len(a) == 0:
        error_a = error_null
    else:
        try:
            a = int(a)
            if a == 0:
                error_a = error_zero
        except:
            error_a = error_not_int

    return {'val': a, 'error': error_a}


def quadratic(request):

    dis_text_null = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    dis_text_result = 'Дискриминант: %(dis)d'

    result_text = 'Квадратное уравнение имеет два действительных корня: x1 = %(x1)d, x2 = %(x2)d'

    a = request.GET['a']
    data = get_val_data(a)
    error_a = data.get('error')
    a = data.get('val')

    b = request.GET['b']
    data = get_val_data(b)
    error_b = data.get('error')
    b = data.get('val')

    c = request.GET['c']
    data = get_val_data(c)
    error_c = data.get('error')
    c = data.get('val')


    result_text_x1_x2 = ''
    if error_a == error_b == error_c == '':
        dis = b ** 2 - 4 * a * c
        dis_result = dis_text_result % {'dis': dis}

        if dis > 0:
            x1 = (-b + math.sqrt(dis)) / 2 * a
            x2 = (-b - math.sqrt(dis)) / 2 * a
            result_text_x1_x2 = result_text % {'x1': x1, 'x2': x2}
        else:
            result_text_x1_x2 = dis_text_null
    else:
        dis_result = ''


    context = {'dis_result': dis_result,
               'result_text_x1_x2': result_text_x1_x2,
               'error_a': error_a,
               'error_b': error_b,
               'error_c': error_c,
               'val_a': a,
               'val_b': b,
               'val_c': c,
               }

    #print(request)
    #print(request.method)
    print(context)
    return render(request, 'results.html', context)
