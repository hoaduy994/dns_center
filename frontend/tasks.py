
from celery.decorators import task
from celery.utils.log import get_task_logger
from support_tools import link_dns_to_b_list,getipsiemtoweb

logger = get_task_logger(__name__)

@task(name="dnsfilter")
def DNS_filter_List_View(title,data_domain,list_add_dns):
    logger.info("DNS filter list view start @_@")
    return link_dns_to_b_list.main(title=title,data_domain=data_domain,list_add_dns=list_add_dns)

@task(name="taskgetipsiemtoweb")
def taskgetipsiemtoweb(ip_siem,port_siem):
    logger.info("taskgetipsiemtoweb start @_@")
    return getipsiemtoweb.main(ip_siem=ip_siem,port_siem=port_siem)