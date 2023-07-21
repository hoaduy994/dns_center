$(function () {
    $('#list_dns_filter_table').DataTable();
  
    $('#list_dns_filter_table').on('click', '.del-filter-list', function() {
      let idIp = $(this).data("iddns")
      idIp = idIp.replace(/'/g, '"');
      idIp = JSON.parse(idIp);
  
      let dns = $(this).data("dnsname")
      dns = dns.replace(/'/g, '"');
      dns = JSON.parse(dns);
  
      let ip = $(this).data("ip")
      ip = ip.replace(/'/g, '"');
      ip = JSON.parse(ip);
  
      let id = $(this).data("id")
  
      idIp.forEach((element, index) => {
        let html = `
        <tr>
          <input name="id" type="hidden" value="${id}">
          <td>
            <div class="form-check">
              <input class="form-check-input" name="idIp" type="checkbox" value="${element}">
            </div>
          </td>
          <td>
            <span>${dns[index]}</span>
          </td>
          <td>
            <span>${ip[index]}</span>
          </td>
        </tr>
      `
        $("#listDnsFilterDel").append(html);
      });
    });
  
    $('#modelDeleteDnsFilter').on('hidden.bs.modal', function (e) {
      $("#listDnsFilterDel").empty();
    })

    $('.btn-submit-dnsfilter').click(function (e) {
      e.preventDefault();
      let domain = $('.domain-dnsfilter').val();
      let title = $('.title-dnsfilter').val();
  
      $('.domain-dnsfilter').keyup(function () {
        $('.domain-dnsfilter-err').css({ "display": "none" });
      });
  
      $('.title-dnsfilter').keyup(function () {
        $('.title-dnsfilter-err').css({ "display": "none" });
      });
  
      if (!ValidateNull(domain)) {
        $('.domain-dnsfilter-err').text("Required fields !");
        $('.domain-dnsfilter-err').css({ "display": "block" });
      } 
  
      if (!ValidateNull(title)) {
        $('.title-dnsfilter-err').text("Title is required !");
        $('.title-dnsfilter-err').css({ "display": "block" });
      }
  
      let checked = $('.checkbox-dnsfilter:checked').length;
  
      if (checked <= 0) {
        $('.checkbox-dnsfilter-err').text("Required fields !");
        $('.checkbox-dnsfilter-err').css({ "display": "block" });
      }
  
      if (ValidateNull(domain) && ValidateNull(title) && checked > 0) {
        $('.form-add-dnsfilter').submit();
      }
    });
  
    // function ValidateDomain(domain) {
    //   if (/^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$/.test(domain)) {
    //     return (true)
    //   }
    //   return (false)
    // }
  
    function ValidateNull(data) {
      data = data.trim().length;
      if (data && data > 0) {
        return (true)
      }
      return (false)
    }
  });
  