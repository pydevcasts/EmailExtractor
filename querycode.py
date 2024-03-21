
from email import encoders
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "siyamak1981@gmail.com"
# body = """  Hi I'm Siyamak
#             I hope you are doing well
#             Full Stack Web Developer with 4 years of practical experience in object-oriented programing and design patterns and extensive experience with PHP and Python.
#             Proven ability in optimizing web functionality that improve data retrieval and workflow efficiencies.
#             I am interested in new and hard challenges and an interest in teamwork.
#             Are there opportunity for me in your company?
#             For more information please download my resume on below or contact with me
#             http://s-abasnezhad.ir
#             whatsapp:+989198859723
#         """
html = """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title>Querycode</title>


    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Merriweather:400,400i,700,700i">

</head>
<style>

.rollover:hover .rollover-second {
    max-height: none !important;
    display: inline-block !important;
  }
  .es-infoblock a:hover {
    color: #ffffff !important;
  }
  .es-footer-body a:hover {
    color: #ffffff !important;
  }
  .es-content-body a:hover {
    color: #eb5757 !important;
  }
  .es-header-body a:hover {
    color: #151D41 !important;
  }
  .es-desk-hidden {
    display: none;
    float: left;
    overflow: hidden;
    width: 0;
    max-height: 0;
    line-height: 0;
    mso-hide: all;
  }
  a[x-apple-data-detectors] {
    color: inherit !important;
    text-decoration: none !important;
    font-size: inherit !important;
    font-family: inherit !important;
    font-weight: inherit !important;
    line-height: inherit !important;
  }
  a.es-button {
    mso-style-priority: 100 !important;
    text-decoration: none !important;
  }
  span.MsoHyperlink,
  span.MsoHyperlinkFollowed {
    color: inherit;
    mso-style-priority: 99;
  }
  #outlook a {
    padding: 0;
  }
  u ~ div img + div > div {
    display: none;
  }
  .rollover div {
    font-size: 0px;
  }
  .rollover:hover .rollover-first {
    max-height: 0px !important;
    display: none !important;
  }
  .es-button-border:hover > a.es-button {
    color: #2f80ed !important;
  }
  *.hover:hover {
    box-shadow: 0 0 20px 0 #999999 !important;
    border-radius: 12px !important;
    border-width: 1px !important;
    display: inline-table !important;
  }
  /*
    END OF IMPORTANT
  */
  a.es-button, button.es-button {
    padding: 10px 25px 10px 25px;
  }
  body {
    width: 100%;
    height: 100%;
  }
  table {
    mso-table-lspace: 0pt;
    mso-table-rspace: 0pt;
    border-collapse: collapse;
    border-spacing: 0px;
  }
  table td,
  body,
  .es-wrapper {
    padding: 0;
    Margin: 0;
  }
  .es-content,
  .es-header,
  .es-footer {
    width: 100%;
    table-layout: fixed !important;
  }
  img {
    display: block;
    font-size: 16px;
    border: 0;
    outline: none;
    text-decoration: none;
  }
  p,
  hr {
    Margin: 0;
  }
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    Margin: 0;
    font-family: 'Roboto Condensed', 'Arial Narrow', Arial, sans-serif;
    mso-line-height-rule: exactly;
    letter-spacing: 0;
  }
  p,
  a {
    mso-line-height-rule: exactly;
  }
  .es-left {
    float: left;
  }
  .es-right {
    float: right;
  }
  .es-menu td {
    border: 0;
  }
  .es-menu td a img {
    display: inline !important;
    vertical-align: middle;
  }
  s {
    text-decoration: line-through;
  }
  a {
    text-decoration: underline;
  }
  .es-menu td a {
    font-family: roboto, 'helvetica neue', helvetica, arial, sans-serif;
    text-decoration: none;
    display: block;
  }
  .es-wrapper {
    width: 100%;
    height: 100%;
    background-repeat: repeat;
    background-position: center top;
  }
  .es-wrapper-color,
  .es-wrapper {
    background-color: #F9F9F9;
  }
  .es-content-body p,
  .es-footer-body p,
  .es-header-body p,
  .es-infoblock p {
    font-family: roboto, 'helvetica neue', helvetica, arial, sans-serif;
    line-height: 150%;
    letter-spacing: 0;
  }
  .es-header {
    background-color: transparent;
    background-repeat: repeat;
    background-position: center top;
  }
  .es-header-body {
    background-color: transparent;
  }
  .es-header-body p {
    color: #6C7083;
    font-size: 18px;
  }
  .es-header-body a {
    color: #151D41;
    font-size: 18px;
  }
  .es-footer {
    background-color: #151D41;
    background-repeat: repeat;
    background-position: center top;
  }
  .es-footer-body {
    background-color: transparent;
  }
  .es-footer-body p {
    color: #ffffff;
    font-size: 16px;
  }
  .es-footer-body a {
    color: #ffffff;
    font-size: 20px;
  }
  .es-content-body {
    background-color: transparent;
  }
  .es-content-body p {
    color: #6C7083;
    font-size: 20px;
  }
  .es-content-body a {
    color: #eb5757;
    font-size: 20px;
  }
  .es-infoblock p {
    font-size: 14px;
    color: #ffffff;
  }
  .es-infoblock a {
    font-size: 14px;
    color: #ffffff;
  }
  h1 {
    font-size: 36px;
    font-style: normal;
    font-weight: normal;
    line-height: 120%;
    color: #151D41;
  }
  .es-header-body h1 a,
  .es-content-body h1 a,
  .es-footer-body h1 a {
    font-size: 36px;
  }
  h2 {
    font-size: 28px;
    font-style: normal;
    font-weight: normal;
    line-height: 120%;
    color: #151D41;
  }
  .es-header-body h2 a,
  .es-content-body h2 a,
  .es-footer-body h2 a {
    font-size: 28px;
  }
  h3 {
    font-size: 24px;
    font-style: normal;
    font-weight: normal;
    line-height: 120%;
    color: #151D41;
  }
  .es-header-body h3 a,
  .es-content-body h3 a,
  .es-footer-body h3 a {
    font-size: 24px;
  }
  h5 {
    font-size: 20px;
    font-style: normal;
    font-weight: normal;
    line-height: 120%;
    color: #333333;
  }
  .es-header-body h5 a,
  .es-content-body h5 a,
  .es-footer-body h5 a {
    font-size: 20px;
  }
  h6 {
    font-size: 16px;
    font-style: normal;
    font-weight: normal;
    line-height: 120%;
    color: #333333;
  }
  .es-header-body h6 a,
  .es-content-body h6 a,
  .es-footer-body h6 a {
    font-size: 16px;
  }
  .es-header-body h4 a,
  .es-content-body h4 a,
  .es-footer-body h4 a {
    font-size: 20px;
  }
  .es-button-border {
    border-style: solid;
    border-color: #2f80ed #2f80ed #2f80ed #2f80ed;
    background: #e1effc;
    border-width: 0px 0px 2px 0px;
    display: inline-block;
    border-radius: 12px 12px 12px 12px;
    width: auto;
    padding:20px;
    mso-hide: all;
  }
  .es-button img {
    display: inline-block;
    vertical-align: middle;
  }
  .es-fw,
  .es-fw .es-button {
    display: block;
  }
  .es-il,
  .es-il .es-button {
    display: inline-block;
  }
  @media only screen and (max-width: 600px) {
    .es-social td {
      padding-bottom: 10px;
    }
    table.es-table-not-adapt,
    .esd-block-html table {
      width: auto !important;
    }
    td.es-desk-menu-hidden {
      display: table-cell !important;
    }
    table.es-desk-hidden {
      display: table !important;
    }
    tr.es-desk-hidden {
      display: table-row !important;
    }
    .es-mobile-hidden,
    .es-hidden {
      display: none !important;
    }
    .adapt-img {
      width: 100% !important;
      height: auto !important;
    }
    .es-content table,
    .es-header table,
    .es-footer table,
    .es-content,
    .es-footer,
    .es-header {
      width: 100% !important;
      max-width: 600px !important;
    }
    .es-adaptive table,
    .es-left,
    .es-right {
      width: 100% !important;
    }
    .es-m-il,
    .es-m-il .es-button,
    .es-social,
    .es-social td,
    .es-menu {
      display: inline-block !important;
    }
    .es-m-fw,
    .es-m-fw.es-fw,
    .es-m-fw .es-button {
      display: block !important;
    }
    a.es-button,
    button.es-button,
    .es-button-border {
      display: inline-block !important;
    }
    a.es-button,
    button.es-button {
      font-size: 16px !important;
      width: 50px;
    }
    .es-spacer {
      display: inline-table;
    }
    .es-m-txt-r .rollover div,
    .es-m-txt-c .rollover div,
    .es-m-txt-l .rollover div {
      line-height: 0 !important;
      font-size: 0 !important;
    }
    .es-m-txt-r .rollover:hover .rollover-second,
    .es-m-txt-c .rollover:hover .rollover-second,
    .es-m-txt-l .rollover:hover .rollover-second {
      display: inline !important;
    }
    .es-m-txt-r img,
    .es-m-txt-c img,
    .es-m-txt-l img {
      display: inline !important;
    }
    .es-m-txt-l,
    .es-m-txt-l h1,
    .es-m-txt-l h2,
    .es-m-txt-l h3,
    .es-m-txt-l h4,
    .es-m-txt-l h5,
    .es-m-txt-l h6 {
      text-align: left !important;
    }
    .es-m-txt-j,
    .es-m-txt-j h1,
    .es-m-txt-j h2,
    .es-m-txt-j h3,
    .es-m-txt-j h4,
    .es-m-txt-j h5,
    .es-m-txt-j h6 {
      text-align: justify !important;
    }
    .es-m-txt-r,
    .es-m-txt-r h1,
    .es-m-txt-r h2,
    .es-m-txt-r h3,
    .es-m-txt-r h4,
    .es-m-txt-r h5,
    .es-m-txt-r h6 {
      text-align: right !important;
    }
    .es-m-txt-c,
    .es-m-txt-c h1,
    .es-m-txt-c h2,
    .es-m-txt-c h3,
    .es-m-txt-c h4,
    .es-m-txt-c h5,
    .es-m-txt-c h6 {
      text-align: center !important;
    }
    .es-infoblock p,
    .es-infoblock a {
      font-size: 14px !important;
    }
    .es-footer-body p,
    .es-footer-body a {
      font-size: 16px !important;
    }
    .es-content-body p,
    .es-content-body a {
      font-size: 16px !important;
    }
    .es-header-body p,
    .es-header-body a {
      font-size: 16px !important;
    }
    .es-header-body h6 a,
    .es-content-body h6 a,
    .es-footer-body h6 a {
      font-size: 16px !important;
    }
    .es-header-body h5 a,
    .es-content-body h5 a,
    .es-footer-body h5 a {
      font-size: 20px !important;
    }
    .es-header-body h4 a,
    .es-content-body h4 a,
    .es-footer-body h4 a {
      font-size: 20px !important;
    }
    .es-header-body h3 a,
    .es-content-body h3 a,
    .es-footer-body h3 a {
      font-size: 20px !important;
    }
    .es-header-body h2 a,
    .es-content-body h2 a,
    .es-footer-body h2 a {
      font-size: 26px !important;
    }
    .es-header-body h1 a,
    .es-content-body h1 a,
    .es-footer-body h1 a {
      font-size: 30px !important;
    }
    h6,
    h6 a {
      line-height: 120% !important;
    }
    h5,
    h5 a {
      line-height: 120% !important;
    }
    h4,
    h4 a {
      line-height: 120% !important;
    }
    h3,
    h3 a {
      line-height: 120% !important;
    }
    h2,
    h2 a {
      line-height: 120% !important;
    }
    h1,
    h1 a {
      line-height: 120% !important;
    }
    p,
    a {
      line-height: 150% !important;
    }
    *[class="gmail-fix"] {
      display: none !important;
    }
    h4 {
      line-height: 120%;
    }
    .h-auto {
      height: auto !important;
    }
    h1 a {
      text-align: left;
    }
    h2 a {
      text-align: left;
    }
    h3 a {
      text-align: left;
    }
    h4 a {
      font-size: 20px !important;
      text-align: left;
    }
    table.w-auto,
      td.w-auto {
      width: auto !important;
    }
    table.w-80,
      td.w-80 {
      width: 80% !important;
    }
    table.w-90,
      td.w-90 {
      width: 90% !important;
    }
  }
  h4 a {
    font-size: 20px;
  }
</style>
<body>
    <div class="es-wrapper-color">
    
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                  
                        <table class="es-header" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" align="center" style="background-color: transparent;">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p20b es-p10r es-p10l" align="left" background="https://xudkfo.stripocdn.email/content/guids/CABINET_4d97b186d58a5e1ea58c9c6185a6936d/images/group_151_2.png" esd-img-prev-position="center center" style="background-image: url(https://xudkfo.stripocdn.email/content/guids/CABINET_4d97b186d58a5e1ea58c9c6185a6936d/images/group_151_2.png); background-repeat: no-repeat; background-position: center center;">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="580" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href="https://querycode.ir/"><img src="https://querycode.ir/wp-content/uploads/2023/05/logo-no-background.png" alt="" style="display:block;height: 100px;padding:100px" width="200" "></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p10r es-p10l" align="left">
                                                        <table cellpadding="0" cellspacing="0" width="100%" style="border-collapse:separate; margin-bottom: 60px;">
                                                            <tbody>
                                                                <tr>

                                                                    <td width="580" class="esd-container-frame" align="center" valign="top" style="border-radius:12px;border-width:1px;border-style:solid;border-color:#e1effc;background-color:#ffffff" bgcolor="#ffffff">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="box-shadow:0px 20px 20px #999999;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text">
                                                                                        <p>🔥 مسیری نوین به دنیای برنامه
                                                                                            نویسی با ما شروع می شود!
                                                                                            🚀 <br></p>
                                                                                        <p>
                                                                                        </p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>


                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p10r es-p10l" align="left">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="580" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text">
                                                                                        <h1> </h1>
                                                                                        <p> </p>
                                                                                        <p>آموزش‌هایی شگفت‌انگیز منتظر
                                                                                            شماست تا همه جزئیات آموزش
                                                                                            برنامه نویسی در سایت را به
                                                                                            شما آموزش دهیم. </p>

                                                                                       
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text">
                                                                                        <h1> </h1>
                                                                                        <p> </p>
                                                                                      
                                                                                            
                                                                                        <p>📚 با ما یادگیری برنامه نویسی
                                                                                            به یک سفر هیجان‌انگیز تبدیل
                                                                                            می‌شود. از مبانی تا مفاهیم
                                                                                            پیچیده، همه چیز در اختیار
                                                                                            شماست. همراهی ما در این
                                                                                            مسیر، شما را به دنیایی از
                                                                                            امکانات جدید و شغل های
                                                                                            برنامه نویسی خواهد برد.</p>
                                                                                        <br><br>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="right" class="esd-block-text">
                                                                                        <p>💡 بهره‌برداری از منابع
                                                                                            آموزشی حرفه‌ای، برنامه‌نویسی
                                                                                            را به یک هنر تبدیل می‌کند.
                                                                                            با پروژه‌های عملی، به
                                                                                            تجربه‌های واقعی دست پیدا
                                                                                            کنید و مهارت‌های خود را در
                                                                                            محیطی تعاملی تقویت کنید.</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                               
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                              
                                                <tr>
                                                    <td class="esd-structure es-p30t es-p10r es-p10l" align="left">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="580" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button">


                                                                                        <!--[if !mso]-->
                                                                                        <!-- --><span class="es-button-border"><a href="https://querycode.ir/" class="es-button" target="_blank" >Querycode.ir</a></span>
                                                                                        <!--<![endif]-->
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p10r es-p10l" align="left">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="580" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank"><img class="adapt-img" src="https://xudkfo.stripocdn.email/content/guids/CABINET_4d97b186d58a5e1ea58c9c6185a6936d/images/verh_1.png" alt="" style="display: block;" width="580"></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                                <tr>
                                                                    <td width="580" class="esd-container-frame" align="center" valign="top" style="background-color:#219653;background-image:url(https://xudkfo.stripocdn.email/content/guids/CABINET_4d97b186d58a5e1ea58c9c6185a6936d/images/seredina_1.png);background-repeat:no-repeat;background-position:center center;background-size:100% 100%" bgcolor="#219653" background="https://xudkfo.stripocdn.email/content/guids/CABINET_4d97b186d58a5e1ea58c9c6185a6936d/images/seredina_1.png">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" esd-img-prev-position="center center">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p20t es-p30r es-p30l">
                                                                                        <p style="color:#1c1b1b">🖥️ با
                                                                                            استفاده از ابزارها و
                                                                                            تکنولوژی‌های روز دنیای
                                                                                            تکنولوژی را کشف کنید و به
                                                                                            رشد شخصی و حرفه‌ای خود
                                                                                            پله‌های بلندی بزنید.</p><br>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-footer" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center" style="background-color: #151d41;" bgcolor="#151d41">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20b es-p10r es-p10l" align="right">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="580" class="esd-container-frame" align="center" valign="top" style="background-color:#219653;background-image:url(https://xudkfo.stripocdn.email/content/guids/CABINET_4d97b186d58a5e1ea58c9c6185a6936d/images/seredina_2.png);background-repeat:no-repeat;background-position:center center;background-size:100% 100%" bgcolor="#219653" background="https://xudkfo.stripocdn.email/content/guids/CABINET_4d97b186d58a5e1ea58c9c6185a6936d/images/seredina_2.png">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" esd-img-prev-position="center center">
                                                                            <tbody>
                                                                             
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-button es-p10b">


                                                                                 
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                                <tr>
                                                                    <td width="580" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank"><img class="adapt-img" src="https://xudkfo.stripocdn.email/content/guids/CABINET_4d97b186d58a5e1ea58c9c6185a6936d/images/niz_1.png" alt="" style="display: block;" width="580"></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p10r es-p10l" align="right">
                                                        <!--[if mso]><table width="580" cellpadding="0" cellspacing="0"><tr><td width="180" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" align="right" class="es-left">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="150" class="esd-container-frame es-m-p20b" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="right" class="esd-block-text es-m-txt-c">
                                                                                        <h3 style="color:#ffffff;padding-top:20px;line-height:120% !important">
                                                                                            تماس با ما</h3>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="right" class="esd-block-text es-p10t es-m-txt-c">
                                                                                        <p style="line-height: 200%;color: white;">
                                                                                            ایمیل:
                                                                                            <span style="color:white">
                                                                                            querycode@querycode.ir
                                                                                            </span>
                                                                                            <br>
                                                                                            تلفن:
                                                                                            <a target="_blank" href="tel:" style="line-height: 200%;color:white">09112137104-
                                                                                                9198859723</a>
                                                                                                </p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td class="es-hidden" width="30"></td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="190" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="190" class="esd-container-frame es-m-p20b" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="right" class="esd-block-text es-m-txt-c">
                                                                                        <h3 style="color: #ffffff;padding-top:20px;float:right">
                                                                                            درباره ما</h3>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="right" class="esd-block-text es-p10t es-m-txt-c">
                                                                                        <p style="color:white">"کوئری کد" جایی است که
                                                                                            برنامه‌نویسان به رشد
                                                                                            می‌پردازند. قدرت اجتماعی،
                                                                                            لذت یادگیری مشترک و پتانسیل
                                                                                            بهبود مهارت‌های برنامه‌نویسی
                                                                                            خود را از طریق "کوئری کد"
                                                                                            بپذیرید. سفر به تبدیل شدن به
                                                                                            یک برنامه‌نویس بهتر از اینجا
                                                                                            آغاز می‌شود.</p><br>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="30"></td><td width="180" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="180" class="esd-container-frame es-m-p20b" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="right" class="esd-block-image es-m-txt-c" style="font-size: 0px; padding-top:20px"><a target="_blank" href="https://querycode.ir/"><img src="https://querycode.ir/wp-content/uploads/2023/05/logo-no-background.png" alt="" style="display:block" width="130"></a>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="right" class="esd-block-social es-p10t es-m-txt-c" style="font-size:0">
                                                                                        <table cellpadding="0" cellspacing="0" class="es-table-not-adapt es-social">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                 
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr >
                                                    <td class="esd-structure es-p40t es-p40b es-p10r es-p10l" align="right" >
                                                        <table cellpadding="0" cellspacing="0" width="100%"style="margin-top:50px">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="580" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text">
                                                                                        <p>© Copyright 2021 
                                                                                         
                                                                                        </p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    
                       
                    </td>
                </tr>
            </tbody>
        </table>
    </div>



</body></html>






    """
password = input("what is your password of your email? ")


context = ssl.create_default_context()
with open("Emails/ExtractEmailNezamMohandesiKerman.txt", 'r') as f:
    emlist = f.readlines()
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)

    for email in emlist:
        receiver_email = email
        message = MIMEMultipart("alternative")
        message["Subject"] = "آموزش  برنامه نویسی"
        message["From"] = sender_email
        message["To"] = receiver_email
        print(message["To"])
        message["Bcc"] = receiver_email
        message.attach(MIMEText(html, "html"))

        # filename="resume.pdf"
        # with open(filename, "rb") as attachment:
        #     part = MIMEBase("application", "octet-stream")
        #     part.set_payload(attachment.read())

        # encoders.encode_base64(part)
        # part.add_header(
        #     "Content-Disposition",
        #     f"attachment; filename= {filename}",
        # )

        # message.attach(part)
        # text = message.as_string()
        # part1 = MIMEText(text, "plain")
        # message.attach(part1)

        server.sendmail(sender_email, receiver_email, message.as_string())
except Exception as e:
    print(e)
finally:
    print("whole of them is done good luck!")
    server.quit()
