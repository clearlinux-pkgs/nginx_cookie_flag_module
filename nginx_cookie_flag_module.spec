#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nginx_cookie_flag_module
Version  : 1.1.0
Release  : 23
URL      : https://github.com/AirisX/nginx_cookie_flag_module/archive/v1.1.0.tar.gz
Source0  : https://github.com/AirisX/nginx_cookie_flag_module/archive/v1.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: nginx_cookie_flag_module-lib = %{version}-%{release}
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev

%description
The Nginx module for adding cookie flag
==========
[![License](http://img.shields.io/badge/license-BSD-brightgreen.svg)](https://github.com/Airis777/nginx_cookie_flag_module/blob/master/LICENSE)

%package lib
Summary: lib components for the nginx_cookie_flag_module package.
Group: Libraries

%description lib
lib components for the nginx_cookie_flag_module package.


%prep
%setup -q -n nginx_cookie_flag_module-1.1.0
cd %{_builddir}/nginx_cookie_flag_module-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nginx-module configure
nginx-module build

%install
nginx-module install %{buildroot}


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_cookie_flag_filter_module.so
