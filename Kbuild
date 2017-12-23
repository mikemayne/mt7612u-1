obj-$(CONFIG_MT76_CORE) += mt76.o
obj-$(CONFIG_MT76x2E) += mt76x2e.o

obj-m := mt76.o mt76x2e.o

mt76-y := \
	mt76/mmio.o \
	mt76/util.o \
	mt76/trace.o \
	mt76/dma.o \
	mt76/mac80211.o \
	mt76/debugfs.o \
	mt76/eeprom.o \
	mt76/tx.o

CFLAGS_trace.o := -I$(src)

mt76x2e-y := \
	mt76/mt76x2_pci.o \
	mt76/mt76x2_dma.o \
	mt76/mt76x2_main.o \
	mt76/mt76x2_init.o \
	mt76/mt76x2_debugfs.o \
	mt76/mt76x2_tx.o \
	mt76/mt76x2_core.o \
	mt76/mt76x2_mac.o \
	mt76x2_eeprom.o \
	mt76/mt76x2_mcu.o \
	mt76/mt76x2_phy.o \
	mt76/mt76x2_dfs.o \
	mt76/mt76x2_trace.o

CFLAGS_mt76x2_trace.o := -I$(src)
