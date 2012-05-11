%global srcname trml2pdf

Name:           python-trml2pdf12
Version:        1.2
Release:        4%{?dist}
Provides:       python-trml2pdf = %{version}-%{release}
Obsoletes:      python-trml2pdf < 1.2-3
Summary:        Tiny RML2PDF is a tool to easily create PDF documents without programming

Group:          Development/Languages
License:        LGPLv2+
URL:            http://www.satchmoproject.com/snapshots/
Source0:        http://www.satchmoproject.com/snapshots/%{srcname}-%{version}.tar.gz
Source1:        http://svn.debian.org/viewsvn/python-modules/packages/python-trml2pdf/trunk/debian/%{srcname}.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       python-reportlab >= 2.1
# Python-Imaging (PIL) if you use bitmap pictures
Requires:       python-imaging


%description
Convert Report Markup Language (RML) files to PDF.

This is a compat package for programs which still need version 1.2.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{__python} -c 'import setuptools; execfile("setup.py")' bdist_egg


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{python_sitelib}
easy_install -m --prefix $RPM_BUILD_ROOT%{_usr} dist/*.egg
find $RPM_BUILD_ROOT%{python_sitelib} -type f -exec chmod -x \{\} \;
# copy man page
install -m 755 -d ${RPM_BUILD_ROOT}/%{_mandir}/man1
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_mandir}/man1/trml2pdf12.1
# upsteam is a bit dead, so there's no one to extract a script from the module
chmod +x ${RPM_BUILD_ROOT}/%{python_sitelib}/TRML2PDF-1.0-py2.7.egg/trml2pdf/trml2pdf.py
install -m 755 -d ${RPM_BUILD_ROOT}/%{_bindir}
ln -s %{python_sitelib}/TRML2PDF-1.0-py2.7.egg/trml2pdf/trml2pdf.py ${RPM_BUILD_ROOT}/%{_bindir}/trml2pdf12

 
%files
%defattr(-,root,root,-)
%doc COPYRIGHT.txt INSTALL.txt LICENSE.txt README.txt
%{python_sitelib}/*
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Fri May 11 2012 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-4
- Package python-trml2pdf12 as an egg

* Thu May 10 2012 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-3
- Rename to python-trml2pdf12 (FPC #171)

* Tue Nov 09 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-2
- Add man page (from Debian)

* Mon Nov 08 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-1
- Initial package
