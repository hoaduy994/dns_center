$(function () {
  // $('#blacklist_table').DataTable();

  $('#blacklist_table').on('click', '.del-black-list', function () {
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
      $("#listBlackListDel").append(html);
    });
  });

  $('#modelDeleteBlackList').on('hidden.bs.modal', function (e) {
    $("#listBlackListDel").empty();
  })

  $('.btn-submit-blacklist').click(function (e) {
    e.preventDefault();
    let domain = $('.domain-blacklist').val();
    let title = $('.title-blacklist').val();

    $('.domain-blacklist').keyup(function () {
      $('.domain-blacklist-err').css({ "display": "none" });
    });

    $('.title-blacklist').keyup(function () {
      $('.title-blacklist-err').css({ "display": "none" });
    });

    if (!ValidateNull(domain)) {
      $('.domain-blacklist-err').text("Required fields !");
      $('.domain-blacklist-err').css({ "display": "block" });
    } 

    if (!ValidateNull(title)) {
      $('.title-blacklist-err').text("Title is required !");
      $('.title-blacklist-err').css({ "display": "block" });
    }

    let checked = $('.checkbox-blacklist:checked').length;

    if (checked <= 0) {
      $('.checkbox-blacklist-err').text("Required fields !");
      $('.checkbox-blacklist-err').css({ "display": "block" });
    }

    if (ValidateNull(domain) && ValidateNull(title) && checked > 0) {
      $('.form-add-blacklist').submit();
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

  // # Nếu type == 0 : Đây là white
  // # Nếu type == 1 : Đây là black
  // # Nếu type == 2 : Đây là regex_white
  // # Nếu type == 3 : Đây là regex_black
