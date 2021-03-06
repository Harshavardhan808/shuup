# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2020, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.views.generic import DeleteView

from shuup.core.models import ContactGroup
from shuup.utils.django_compat import reverse_lazy


class ContactGroupDeleteView(DeleteView):
    model = ContactGroup
    success_url = reverse_lazy("shuup_admin:contact_group.list")
