from django.shortcuts import render
from django.views import View

class DashboardView(View):
    def get(self, request):
        # Bu yerda ma'lumotlarni bazadan olish va contextga joylash kerak
        context = {
            'page_title': 'Dashboard v3',
            'visitors_data': {
                'current': 820,
                'change': 12.5,
                'series': [
                    {'name': 'High - 2023', 'data': [100, 120, 170, 167, 180, 177, 160]},
                    {'name': 'Low - 2023', 'data': [60, 80, 70, 67, 80, 77, 100]}
                ]
            },
            'sales_data': {
                'current': 18230,
                'change': 33.1,
                'series': [
                    {'name': 'Net Profit', 'data': [44, 55, 57, 56, 61, 58, 63, 60, 66]},
                    {'name': 'Revenue', 'data': [76, 85, 101, 98, 87, 105, 91, 114, 94]},
                    {'name': 'Free Cash Flow', 'data': [35, 41, 36, 26, 45, 48, 52, 53, 41]}
                ]
            },
            'products': [
                {'name': 'Some Product', 'price': 13, 'change': 12, 'sold': 12000, 'image': 'default-150x150.png'},
                {'name': 'Another Product', 'price': 29, 'change': -0.5, 'sold': 123234, 'image': 'default-150x150.png'},
                {'name': 'Amazing Product', 'price': 1230, 'change': -3, 'sold': 198, 'image': 'default-150x150.png'},
                {'name': 'Perfect Item', 'price': 199, 'change': 63, 'sold': 87, 'image': 'default-150x150.png', 'new': True}
            ],
            'metrics': [
                {'icon': 'bi-graph-up-arrow', 'value': 12, 'label': 'CONVERSION RATE', 'color': 'success'},
                {'icon': 'bi-graph-up-arrow', 'value': 0.8, 'label': 'SALES RATE', 'color': 'info'},
                {'icon': 'bi-graph-down-arrow', 'value': -1, 'label': 'REGISTRATION RATE', 'color': 'danger'}
            ]
        }
        return render(request, 'index.html', context)