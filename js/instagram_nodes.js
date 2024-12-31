import { app } from "../../../scripts/app.js";

app.registerExtension({
  name: "Instagram.Downloader",
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (
      nodeData.name === "InstagramDownloader" ||
      nodeData.name === "MediaOrganizer"
    ) {
      const onExecuted = nodeType.prototype.onExecuted;
      nodeType.prototype.onExecuted = function (message) {
        if (onExecuted) {
          onExecuted.apply(this, arguments);
        }
        this.bgcolor = message.success ? "#353" : "#533";
        this.setDirtyCanvas(true);
      };
    }
  },
  nodeCategories: {
    instagram: {
      title: "Instagram",
      color: "#5865F2",
    },
  },
});
