%define product		PasswordResetTool
%define realVersion     0.4.2
%define release         1

%define version %(echo %{realVersion} | sed -e 's/-/./g')

%define zope_minver	2.7
%define plone_minver	2.0

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Summary:	Add a "reset my password" facility
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		System/Servers
Source:		http://plone.org/products/passwordresettool/releases/%{version}/PasswordResetTool-%{realVersion}.tar.bz2
URL:		http://plone.org/products/passwordresettool/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}
Requires:	plone >= %{plone_minver}

Provides:	plone-Faq == %{version}
Obsoletes:	zope-Faq


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
%setup -c

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a %{product} %{buildroot}%{software_home}/Products/%{product}


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
%defattr(0644, root, root, 0755)
%{software_home}/Products/*


