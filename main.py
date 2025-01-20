# import vt
#
# client = vt.Client("01981a7334d54e3ab50bec8b10831aad7f144785f408b4d85ba9e2c9d425e050")
#
# # Get a file report
# file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")
# data = (file.last_analysis_stats)
# def watch_out():
#     for key, value in data.items():
#         if key == "malicious":
#             print("Malicious file detected,\n recommended to delete the file.")
#             break
#         else:
#             print("No malicious file detected, file is safe to use")
#             break
# def detect_summary():
#     print("Threat Detection Summary".center(40, "-"))
#     print(f"{'Category':<20}{'Count':<20}")
#     print("-" * 40)
#     for category, count in data.items():
#         print(f"{category:<20}{count:<20}")
# detect_summary()
# client.close()
# print("")
# print("analysis completed".center(40, "_"))
# watch_out()
