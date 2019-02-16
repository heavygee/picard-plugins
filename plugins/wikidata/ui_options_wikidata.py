# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_wikidata.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WikidataOptionsPage(object):
    def setupUi(self, WikidataOptionsPage):
        WikidataOptionsPage.setObjectName("WikidataOptionsPage")
        WikidataOptionsPage.resize(602, 512)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(WikidataOptionsPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.releaseGroup_groupBox = QtWidgets.QGroupBox(WikidataOptionsPage)
        self.releaseGroup_groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.releaseGroup_groupBox.sizePolicy().hasHeightForWidth())
        self.releaseGroup_groupBox.setSizePolicy(sizePolicy)
        self.releaseGroup_groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.releaseGroup_groupBox.setObjectName("releaseGroup_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.releaseGroup_groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.use_release_group_genres = QtWidgets.QCheckBox(self.releaseGroup_groupBox)
        self.use_release_group_genres.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_release_group_genres.sizePolicy().hasHeightForWidth())
        self.use_release_group_genres.setSizePolicy(sizePolicy)
        self.use_release_group_genres.setChecked(True)
        self.use_release_group_genres.setObjectName("use_release_group_genres")
        self.verticalLayout_4.addWidget(self.use_release_group_genres)
        self.verticalLayout_2.addWidget(self.releaseGroup_groupBox)
        self.artist_groupBox = QtWidgets.QGroupBox(WikidataOptionsPage)
        self.artist_groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artist_groupBox.sizePolicy().hasHeightForWidth())
        self.artist_groupBox.setSizePolicy(sizePolicy)
        self.artist_groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.artist_groupBox.setObjectName("artist_groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.artist_groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.use_artist_genres = QtWidgets.QCheckBox(self.artist_groupBox)
        self.use_artist_genres.setObjectName("use_artist_genres")
        self.verticalLayout_8.addWidget(self.use_artist_genres)
        self.hLayout_use_artist_no_release = QtWidgets.QHBoxLayout()
        self.hLayout_use_artist_no_release.setObjectName("hLayout_use_artist_no_release")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_use_artist_no_release.addItem(spacerItem)
        self.use_artist_only_if_no_release = QtWidgets.QCheckBox(self.artist_groupBox)
        self.use_artist_only_if_no_release.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_artist_only_if_no_release.sizePolicy().hasHeightForWidth())
        self.use_artist_only_if_no_release.setSizePolicy(sizePolicy)
        self.use_artist_only_if_no_release.setCheckable(True)
        self.use_artist_only_if_no_release.setChecked(False)
        self.use_artist_only_if_no_release.setObjectName("use_artist_only_if_no_release")
        self.hLayout_use_artist_no_release.addWidget(self.use_artist_only_if_no_release)
        self.verticalLayout_8.addLayout(self.hLayout_use_artist_no_release)
        self.hLayout_ignore_genres_from_artists_label = QtWidgets.QHBoxLayout()
        self.hLayout_ignore_genres_from_artists_label.setObjectName("hLayout_ignore_genres_from_artists_label")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_ignore_genres_from_artists_label.addItem(spacerItem1)
        self.ignore_genres_from_these_artists_label = QtWidgets.QLabel(self.artist_groupBox)
        self.ignore_genres_from_these_artists_label.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_genres_from_these_artists_label.sizePolicy().hasHeightForWidth())
        self.ignore_genres_from_these_artists_label.setSizePolicy(sizePolicy)
        self.ignore_genres_from_these_artists_label.setObjectName("ignore_genres_from_these_artists_label")
        self.hLayout_ignore_genres_from_artists_label.addWidget(self.ignore_genres_from_these_artists_label)
        self.verticalLayout_8.addLayout(self.hLayout_ignore_genres_from_artists_label)
        self.hLayout_ignore_genres_from_artists = QtWidgets.QHBoxLayout()
        self.hLayout_ignore_genres_from_artists.setObjectName("hLayout_ignore_genres_from_artists")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_ignore_genres_from_artists.addItem(spacerItem2)
        self.ignore_genres_from_these_artists = QtWidgets.QLineEdit(self.artist_groupBox)
        self.ignore_genres_from_these_artists.setEnabled(False)
        self.ignore_genres_from_these_artists.setObjectName("ignore_genres_from_these_artists")
        self.hLayout_ignore_genres_from_artists.addWidget(self.ignore_genres_from_these_artists)
        self.verticalLayout_8.addLayout(self.hLayout_ignore_genres_from_artists)
        self.verticalLayout_2.addWidget(self.artist_groupBox)
        self.work_groupBox = QtWidgets.QGroupBox(WikidataOptionsPage)
        self.work_groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_groupBox.sizePolicy().hasHeightForWidth())
        self.work_groupBox.setSizePolicy(sizePolicy)
        self.work_groupBox.setObjectName("work_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.work_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.use_work_genres = QtWidgets.QCheckBox(self.work_groupBox)
        self.use_work_genres.setChecked(True)
        self.use_work_genres.setObjectName("use_work_genres")
        self.verticalLayout_3.addWidget(self.use_work_genres)
        self.verticalLayout_2.addWidget(self.work_groupBox)
        self.generalSettings_groupBox = QtWidgets.QGroupBox(WikidataOptionsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generalSettings_groupBox.sizePolicy().hasHeightForWidth())
        self.generalSettings_groupBox.setSizePolicy(sizePolicy)
        self.generalSettings_groupBox.setMinimumSize(QtCore.QSize(0, 120))
        self.generalSettings_groupBox.setObjectName("generalSettings_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.generalSettings_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ignore_genres_label = QtWidgets.QLabel(self.generalSettings_groupBox)
        self.ignore_genres_label.setObjectName("ignore_genres_label")
        self.verticalLayout.addWidget(self.ignore_genres_label)
        self.hLayout_ignore_these_genres = QtWidgets.QHBoxLayout()
        self.hLayout_ignore_these_genres.setObjectName("hLayout_ignore_these_genres")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_ignore_these_genres.addItem(spacerItem3)
        self.ignore_these_genres = QtWidgets.QLineEdit(self.generalSettings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_these_genres.sizePolicy().hasHeightForWidth())
        self.ignore_these_genres.setSizePolicy(sizePolicy)
        self.ignore_these_genres.setObjectName("ignore_these_genres")
        self.hLayout_ignore_these_genres.addWidget(self.ignore_these_genres)
        self.verticalLayout.addLayout(self.hLayout_ignore_these_genres)
        self.genre_delimiter_label = QtWidgets.QLabel(self.generalSettings_groupBox)
        self.genre_delimiter_label.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genre_delimiter_label.sizePolicy().hasHeightForWidth())
        self.genre_delimiter_label.setSizePolicy(sizePolicy)
        self.genre_delimiter_label.setWordWrap(False)
        self.genre_delimiter_label.setObjectName("genre_delimiter_label")
        self.verticalLayout.addWidget(self.genre_delimiter_label)
        self.hLayout_genre_delimiter = QtWidgets.QHBoxLayout()
        self.hLayout_genre_delimiter.setObjectName("hLayout_genre_delimiter")
        spacerItem4 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_genre_delimiter.addItem(spacerItem4)
        self.genre_delimiter = QtWidgets.QComboBox(self.generalSettings_groupBox)
        self.genre_delimiter.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genre_delimiter.sizePolicy().hasHeightForWidth())
        self.genre_delimiter.setSizePolicy(sizePolicy)
        self.genre_delimiter.setEditable(True)
        self.genre_delimiter.setObjectName("genre_delimiter")
        self.genre_delimiter.addItem("")
        self.genre_delimiter.setItemText(0, " / ")
        self.genre_delimiter.addItem("")
        self.genre_delimiter.addItem("")
        self.genre_delimiter.setItemText(2, ";")
        self.genre_delimiter.addItem("")
        self.genre_delimiter.addItem("")
        self.genre_delimiter.setItemText(4, ", ")
        self.hLayout_genre_delimiter.addWidget(self.genre_delimiter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_genre_delimiter.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.hLayout_genre_delimiter)
        self.verticalLayout_2.addWidget(self.generalSettings_groupBox)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)

        self.retranslateUi(WikidataOptionsPage)
        self.use_artist_genres.toggled['bool'].connect(self.ignore_genres_from_these_artists_label.setEnabled)
        self.use_artist_genres.toggled['bool'].connect(self.use_artist_only_if_no_release.setEnabled)
        self.use_artist_genres.toggled['bool'].connect(self.ignore_genres_from_these_artists.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(WikidataOptionsPage)

    def retranslateUi(self, WikidataOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.releaseGroup_groupBox.setTitle(_translate("WikidataOptionsPage", "Release Group Genre Settings"))
        self.use_release_group_genres.setText(_translate("WikidataOptionsPage", "Use Release Group genres"))
        self.artist_groupBox.setTitle(_translate("WikidataOptionsPage", "Artist Genre Settings"))
        self.use_artist_genres.setText(_translate("WikidataOptionsPage", "Use Artist genres"))
        self.use_artist_only_if_no_release.setText(_translate("WikidataOptionsPage", "Use Artist genres only if no Release Group genres exist"))
        self.ignore_genres_from_these_artists_label.setText(_translate("WikidataOptionsPage", "Ignore Artist genres from these Artist(s):  (comma separated regular expressions)"))
        self.work_groupBox.setTitle(_translate("WikidataOptionsPage", "Work Genre Settings"))
        self.use_work_genres.setText(_translate("WikidataOptionsPage", "Use Work genres, when applicable"))
        self.generalSettings_groupBox.setTitle(_translate("WikidataOptionsPage", "General Settings"))
        self.ignore_genres_label.setText(_translate("WikidataOptionsPage", "Ignore these genres:   (comma separated regular expressions)"))
        self.genre_delimiter_label.setText(_translate("WikidataOptionsPage", "Genre Delimiter: (only applicable to ID3v2.3 tags)"))
        self.genre_delimiter.setItemText(1, _translate("WikidataOptionsPage", "; "))
        self.genre_delimiter.setItemText(3, _translate("WikidataOptionsPage", " ; "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WikidataOptionsPage = QtWidgets.QWidget()
    ui = Ui_WikidataOptionsPage()
    ui.setupUi(WikidataOptionsPage)
    WikidataOptionsPage.show()
    sys.exit(app.exec_())

