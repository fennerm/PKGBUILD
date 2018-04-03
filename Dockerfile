FROM oblique/archlinux-pacaur

MAINTAINER Fenner Macrae <fmacrae.dev@gmail.com>

# Test whether a PKGBUILD builds correctly in a clean arch install

RUN pacman --noconfirm --needed -S namcap

USER aur
WORKDIR /home/aur
ARG pkgbuild=""
COPY --chown=aur $pkgbuild /home/aur/PKGBUILD
RUN source /home/aur/PKGBUILD && \
        pacaur --noedit --noconfirm --needed -S ${depends[@]} ${makedepends[@]}
CMD makepkg --noconfirm -si PKGBUILD
