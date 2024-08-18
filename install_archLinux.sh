#!/bin/bash

echo "Setting up / partition"
read -p "Digite o nome da partição: " opcao
yes | mkfs.ext4 /dev/$opcao
mount /dev/$opcao /mnt
mkdir /mnt/home
mkdir /mnt/boot
#clear
echo "Installing Arch Linux"
yes '' | pacstrap /mnt base linux linux-firmware
#clear
echo "Generating fstab"
genfstab -U /mnt >> /mnt/etc/fstab
clear
cat /mnt/etc/fstab
echo "Configuring new system"
arch-chroot /mnt /bin/bash <<EOF
pacman -S nano sudo networkmanager network-manager-applet --noconfirm
echo "Setting system clock"
ln -sf /usr/share/zoneinfo/America/Belem /etc/localtime
hwclock --systohc --localtime
echo "Setting locales"
echo "pt_BR.UTF-8 UTF-8" >> /etc/locale.gen
echo "LANG=pt_BR.UTF-8" >> /etc/locale.conf
locale-gen
echo "Adding persistent keymap"
echo "KEYMAP=br-abnt2" > /etc/vconsole.conf
echo "Setting hostname"
echo arch > /etc/hostname

echo "Setting root password"
echo -en "123\n123" | passwd

echo "Creating new user"
useradd -m -G wheel -s /bin/bash user
usermod -a -G video user
echo -en "123\n123" | passwd user

echo -e "127.0.0.1\tlocalhost\n::1\tlocalhost\n127.0.1.1\tarch.localdomain arch" >> /ett/hosts
cat /etc/hosts

echo "mkinitcpio"
mkinitcpio -P

echo -e "Defaults env_reset,pwfeedback" >> /etc/sudoers
clear

echo "GRUB"
pacman -S grub dosfstools os-prober mtools --noconfirm
grub-install --recheck /dev/$opcao
grub-mkconfig -o /boot/grub/grub.cfg

systemctl enable NetworkManager
systemctl start NetworkManager
exit
umount -R /mnt
EOF
