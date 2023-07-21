from celery import shared_task
# from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from celery.utils.log import get_task_logger
from support_tools import link_dns_to_b_list,get_log_dns_node

logger = get_task_logger(__name__)
@shared_task
def add(x, y):
    return x + y

@task(name="DNS_filter_List")
def DNS_filter_List_View(title,data_domain,do_not_add_dns):
    logger.info("DNS filter list view start @_@")
    return link_dns_to_b_list.main(title=title,data_domain=data_domain,do_not_add_dns=do_not_add_dns)


@task(name="LogToFilelList")
def LogToFilelListView(dns_center_id,file_log):
    logger.info("LogToFilelList@_@")
    return get_log_dns_node.main(dns_center_id=dns_center_id,file_log=file_log)