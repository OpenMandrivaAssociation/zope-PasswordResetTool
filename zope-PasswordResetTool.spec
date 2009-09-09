%define Product PasswordResetTool
%define product passwordresettool
%define name    zope-%{Product}
%define version 1.0
%define release %mkrel 5

%define zope_minver	2.7
%define plone_minver	2.0

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Add a "reset my password" facility
License:	GPL
Group:		System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:	zope >= %{zope_minver}
Requires:	zope-Plone >= %{plone_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The Password Reset Tool hooks into the standard mechanisms for password
mailing provided by the CMF in the Registration Tool and certain skins
and replaces this with a facility for resetting passwords with email
authentication.
This is useful not only to keep passwords out of cleartext email and is
absolutely necessary if you choose to encrypt your passwords (and you
should.)
Note, of course, that you must have a working MailHost to send email!
This tool has been made with customization in mind. There are several
customization points in the code that should allow you to change certain
policies simply by subclassing the tool and overriding one or two
methods.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a %{Product} %{buildroot}%{software_home}/Products/%{Product}


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
